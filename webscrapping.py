from bs4 import BeautifulSoup
import requests
import re

def organizar_scrapping(dados_limpados):
    times = []
    for i in range(0, len(dados_limpados), 9):  # Cada time ocupa 9 posições na lista
        time = {
        "Posição": dados_limpados[i],
        "Time": dados_limpados[i+1],
        "Jogos": dados_limpados[i+2],
        "Vitórias": dados_limpados[i+3],
        "Empates": dados_limpados[i+4],
        "Derrotas": dados_limpados[i+5],
        "Gols": dados_limpados[i+6],
        "Saldo de Gols": dados_limpados[i+7],
        "Pontos": dados_limpados[i+8]
    }
        times.append(time)
        
    return times


def main():
    url = "https://www.worldfootball.net/schedule/bra-serie-a-2020-spieltag/38/"

    html = requests.get(url).text


    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find_all('td')

    filtro = table[82:283] #filtrando o html

    # Limpando espaços extras e exibindo os dados
    dados_limpos = [re.sub(r'\s+', ' ', td.text.strip()) for td in filtro]
    dados_limpos = list(filter(None, dados_limpos)) # Removendo elementos vazios

    # Exibindo os primeiros elementos para verificar a limpeza
    times = organizar_scrapping(dados_limpos)
    # Exibindo os dados de forma organizada
    for time in times:
        print(time)

if(__name__ == "__main__"):
    main()