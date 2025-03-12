import requests
import csv

# Nesta API conseguimos apenas os dados de 2024.
def save_standings_to_csv_2024(standings, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Temporada","Posicao", "Time", "Pontos", "Saldo de Gols", "Jogos", "Vitorias", "Empates", "Derrotas",
                          "Gols marcados", "Gols sofridos"])
            
        data = standings['standings'][0]['table']
        season = standings['filters']['season']
        for team in data:
            writer.writerow([
                        season,
                        team["position"],
                        team["team"]["name"],
                        team["points"],
                        team["goalDifference"],
                        team["playedGames"],
                        team["won"],
                        team["draw"],
                        team["lost"],
                        team["goalsFor"],
                        team["goalsAgainst"],
                        ])


def main():
    id = "2013"

    years = range(2017, 2021)

    
    url = f"https://api.football-data.org/v4/competitions/{id}/standings?season=2024"

    headers = {
        "X-Auth-Token": "0d2559c86395449e813adf4c16af6d3c"
        }
    response = requests.get(url, headers=headers)

    data = response.json()
    save_standings_to_csv_2024(data, "brasileirao_2024.csv")

if (__name__ == "__main__"):
    main()