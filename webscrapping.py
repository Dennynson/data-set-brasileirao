from bs4 import BeautifulSoup
import requests



url = "https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:1223"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

rank = soup.find_all("div", attrs={'class':"sc-e2d69017-1 Vcqyy", 'color':'onSurface.nLv1'})

times = soup.find_all("div", class_="Text fsoviT")


print(rank)
#for classificacao in rank:
    #print(classificacao.text)

#for time in times:
    #print(time.text)