from bs4 import *
import requests
from pandas import *

url = "https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")

movieList = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movieNameNumberList = [movieName.getText().split()[0] for movieName in movieList]
movieActualNameList = [' '.join(movieName.getText().split()[1:]) for movieName in movieList]
extractedTagFromList = [movieName.name for movieName in movieList]
extractedClassFromList = [movieName['class'][0] for movieName in movieList]

divList = soup.find_all(name = "div", class_ = "listicleItem_listicle-item__content__Lxn1Y")
descriptionList = [str(div.find_all(name = "p")[0].text)[:50] for div in divList]

data = {
    "Tag": extractedTagFromList,
    "Class": extractedClassFromList,
    "Movie Number": movieNameNumberList,
    "Movie Name": movieActualNameList,
    "Description": descriptionList,
}

df = DataFrame(data)
with open("Movie.csv", mode = "w") as file:
    file.write(df.to_csv())