from urllib.request import urlopen
from bs4 import BeautifulSoup

#   This function gets the artist name and song title as input and
#   returns the corresponding lyrics as output using Beautiful soup.
def get_lyrics(artist, song):
    try:
        artist = f'{artist.replace(" ", "").lower()}'
        song = f'{song.replace(" ", "").lower()}'
        url = f"https://www.azlyrics.com/lyrics/{artist}/{song}.html"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        main = soup.find(class_="col-xs-12 col-lg-8 text-center")
        divs = main.find_all("div")
        results = [(len(div.text), div.text.strip()) for div in divs]
        lyrics = max(results, key=lambda x: x[0])[1]
        return lyrics
    except Exception as e:
        print(e)
        return ""


#   The function below fetches the top 100 tracks from Billboard.com with the
#   artist name, song title and cover image.
def get_hot_tracks():
    try:
        url = "https://www.billboard.com/charts/hot-100/"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        top100 = soup.select(".o-chart-results-list-row-container")
        covers = [div.find("img")["data-lazy-src"] for div in top100]
        titles = [
            div.select("#title-of-a-story")[0]
            .decode_contents()
            .replace("\n", "")
            .replace("\t", "")
            for div in top100
        ]
        artists = [
            div.find_all("span")[1]
            .decode_contents()
            .replace("\n", "")
            .replace("\t", "")
            for div in top100
        ]
        hot_tracks = [
            {"cover": covers[i], "title": titles[i], "artist": artists[i]}
            for i in range(100)
        ]
        return hot_tracks
    except Exception as e:
        print(e)
        return []