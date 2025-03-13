from bs4 import BeautifulSoup
import requests

def remover_vazios(lista):
    lista_filtrada = []
    for elemento in lista:
        if(elemento == [None]):
            continue
        lista_filtrada.append(elemento)
    
    return lista_filtrada


def organizar_scrapping(filtro):
    dados = []
    for i in range(0, len(filtro)):
        posicao = filtro[i].text.strip()
        time = filtro[i+1].text.strip()
        jogos = filtro[i+2].text.strip()
        vitorias = filtro[i+3].text.strip()
        empates = filtro[i+4].text.strip()
        derrotas = filtro[i+5].text.strip()
        gols_marcados = filtro[i+6].text.strip()
        gols_sofridos = filtro[i+7].text.strip()
        pontos = filtro[i+8].text.strip()
        
        dados.append({
            "Posição": posicao,
            "Time": time,
            "Jogos": jogos,
            "Vitórias": vitorias,
            "Empates": empates,
            "Derrotas": derrotas,
            "Gols marcados": gols_marcados,
            "Gols sofridos": gols_sofridos,
            "Pontos": pontos
        })


    return dados


def main():
    url = "https://www.worldfootball.net/schedule/bra-serie-a-2020-spieltag/38/"

    html = requests.get(url).text


    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find_all('td')

    filtro = table[82:283] #filtrando o html


if(__name__ == "__main__"):
    main()