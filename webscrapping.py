from bs4 import BeautifulSoup
import requests
import csv
import re

# Webscrapping dos dados de 2006-2020 do Campeonato Brasileiro Série A

def organizar_scrapping(dados_limpos, season):
    temporada = []

    for i in range(0, len(dados_limpos), 9):  # Cada time ocupa 9 posições na lista
            gols = dados_limpos[i+6].split(":") #lista com primeiro índice gols marcados, segundo índice gols sofridos
            time = {
            "Temporada" : season,
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
            temporada.append(time)

    return temporada

def save_standings_to_csv(standings, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Temporada","Posicao", "Time", "Pontos", "Saldo de Gols", "Jogos", "Vitorias", "Empates", "Derrotas",
                          "Gols marcados", "Gols sofridos"])
        for temporada in standings:   
            for team in temporada:
                writer.writerow([
                        team["Temporada"],
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

    #falta criar o loop para coletar tudo desde 2020.
    dados_geral = []
    for ano in range(2006, 2021):
        url = f"https://www.worldfootball.net/schedule/bra-serie-a-{ano}-spieltag/38/"

        html = requests.get(url).text


        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find_all('td')

        filtro = table[82:282] #filtrando o html

        # Limpando espaços extras e exibindo os dados
        dados_limpos = [re.sub(r'\s+', ' ', td.text.strip()) for td in filtro]
        dados_limpos = list(filter(None, dados_limpos)) # Removendo elementos vazios

        temporada = organizar_scrapping(dados_limpos, ano)

        dados_geral.append(temporada)


    save_standings_to_csv(dados_geral, "brasileirao_2006_2020.csv")
if(__name__ == "__main__"):
    main()