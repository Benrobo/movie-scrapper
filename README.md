## Movies Scrapper

A basic python script which scrappes movies from the popular site [Thenetnaija.com](https://www.thenetnaija.net/videos/movies/page/1).

### Installation

Install necessary dependencies for this script

```bash
pip install
```

run the file by executing the command below

```bash
python app.py
```

> All generated movies are found within the `movies.json` file in current directory where this script is executed.

To set the script to scrape every movies in thenetnaija website which is currently `228` pages, reste the code below.

Simply comment out the code below which should be from line `94`-`101`

```py
#* if you need to stop scrapping at a specified page count, comment this line below
if page == 3:
    movieJsonFileRead = open("movies.json", "r")
    movieData = movieJsonFileRead.read()
    mvCont = json.loads(movieData)
    movies = mvCont["movies"]
    print(f"Total movies scrapped into 'movies.json' file : {len(movies)}")
    break
```
