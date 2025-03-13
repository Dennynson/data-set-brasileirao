from bs4 import BeautifulSoup
import requests
import csv
import re

def organizar_scrapping(dados_limpos):
    times = []
    for i in range(0, len(dados_limpos), 9):  # Cada time ocupa 9 posições na lista
        gols = dados_limpos[i+6].split(":") #lista com primeiro índice gols marcados, segundo índice gols sofridos
        time = {
        "Posição": dados_limpos[i],
        "Time": dados_limpos[i+1],
        "Pontos": dados_limpos[i+8],
        "Saldo de Gols": dados_limpos[i+7],
        "Jogos": dados_limpos[i+2],
        "Vitórias": dados_limpos[i+3],
        "Empates": dados_limpos[i+4],
        "Derrotas": dados_limpos[i+5],
        "Gols marcados": gols[0],
        "Gols sofridos": gols[1]
    }
        times.append(time)

    return times

def save_standings_to_csv(standings, filename, season):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Temporada","Posicao", "Time", "Pontos", "Saldo de Gols", "Jogos", "Vitorias", "Empates", "Derrotas",
                          "Gols marcados", "Gols sofridos"])
            
        for team in standings:
            writer.writerow([
                    season,
                    team["Posição"],
                    team["Time"],
                    team["Pontos"],
                    team["Saldo de Gols"],
                    team["Jogos"],
                    team["Vitórias"],
                    team["Empates"],
                    team["Derrotas"],
                    team["Gols marcados"],
                    team["Gols sofridos"]
                        ])


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
    '''for time in times:
        print(time)'''
    
    save_standings_to_csv(times, "brasileirao_2020.csv", 2020)

if(__name__ == "__main__"):
    main()