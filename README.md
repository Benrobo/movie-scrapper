## Movies Scrapper

A basic python script which scrappes movies from the popular site [Thenetnaija.com](https://www.thenetnaija.net/videos/movies/page/1).

```json
{
    "movies": [
    {
      "movie_thumbnail": "https://static.netnaija.com/i/AqgKGWZnKr1.webp",
      "movieName": "Mighty Morphin Power Rangers: Once & Always (2023)",
      "movieUrl": "https://www.thenetnaija.net/videos/movies/18510-mighty-morphin-power-rangers-once-always-2023"
    },
    {
      "movie_thumbnail": "https://static.netnaija.com/i/qEQN2rzZN6W.webp",
      "movieName": "A Thousand and One (2023)",
      "movieUrl": "https://www.thenetnaija.net/videos/movies/18507-a-thousand-and-one-2023"
    },
    {
      "movie_thumbnail": "https://static.netnaija.com/i/XV5KvPRGa9m.webp",
      "movieName": "Ant-Man and the Wasp: Quantumania (2023)",
      "movieUrl": "https://www.thenetnaija.net/videos/movies/18505-ant-man-and-the-wasp-quantumania-2023"
    }
}
```

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
