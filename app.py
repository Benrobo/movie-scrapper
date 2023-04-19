from bs4 import BeautifulSoup
import requests
import json


def fetchMovieHtml(url):
    try:
        req = requests.get(url)
        return req.text
    except Exception as e:
        print("Error making requests:", str(e))
        return "null"

def handleFile(data):
    try:
        movieJsonFileRead = open("movies.json", "r")
        movieData = movieJsonFileRead.read()

        if movieData.strip() != "":
            mvCont = json.loads(movieData)
            movies = mvCont["movies"]

            # for obj in data:
            #     if not any(m["movieName"] == obj["movieName"] for m in movies):
            #         movies.append(obj)


            #* This is same has the other commented method above, but much reable.
            for obj in data:
                for movie in movies:
                    if movie["movieName"] == obj["movieName"]:
                        # If the movie already exists in the list, skip adding it
                        break
                else:
                    # If the loop completes without finding a match, add the movie to the list
                    movies.append(obj)
                
            formatedData = json.dumps(mvCont)

            movieJsonFileWrite = open("movies.json", "w")
            movieJsonFileWrite.write(formatedData)
        else: 
            formatedData = { "movies": data } 
            movieJsonFileWrite = open("movies.json", "w")
            movieJsonFileWrite.write(json.dumps(formatedData))
        

    except Exception as e:
        print("Error:", str(e))

def scrapeMovies(movieUrl):
    # fetch page html
    pageContent = fetchMovieHtml(movieUrl)

    if pageContent == "null":
        return None
    
    # handle page content using bsoup
    soup = BeautifulSoup(pageContent, "html.parser")
    movieContainer = soup.find('div', class_='video-files')
    movieArticles = soup.findAll("article", class_='file-one shadow')
    

    # minipulate DOM (Document Object Model)
    allmoviesInfo = []

    for idx, movieArticle in enumerate(movieArticles):
        img_element = movieArticle.find("img", src=True)
        thumbnail_url = img_element['src']
        movieInfo = movieArticle.find("div",class_='info')
        vheading = movieInfo.find('h2')
        vLink = vheading.find("a")
        movieUrl = vLink['href']
        movieName = vLink.text
        
        movieData = {
            "movie_thumbnail": thumbnail_url,
            "movieName": movieName,
            "movieUrl": movieUrl
        }
        allmoviesInfo.append(movieData)
    handleFile(allmoviesInfo)
    return soup
    

def paginatePage(maxPage):
    for page in range(1, maxPage+1):
        MOVIE_URL = "https://www.thenetnaija.net/videos/movies/page/{}".format(page)
        
        # invoke the scrape function
        soup = scrapeMovies(MOVIE_URL)
        print(f"Scrapping {page}")

        #* if you need to stop scrapping at a specified page count, comment this line below
        if page == 3:
            movieJsonFileRead = open("movies.json", "r")
            movieData = movieJsonFileRead.read()
            mvCont = json.loads(movieData)
            movies = mvCont["movies"]
            print(f"Total movies scrapped into 'movies.json' file : {len(movies)}")
            break

        # handle movie paginations
        paginatedContainer = soup.find("ul", class_='pagination')
        allPaginatedList = paginatedContainer.findAll("li")
        lastPaginatedNextBtn = allPaginatedList[len(allPaginatedList) - 1]
        link = lastPaginatedNextBtn.find('a', class_='next page-numbers')

        if not link:
            break
            

MAX_MOVIE_PAGE = 228
paginatePage(MAX_MOVIE_PAGE)