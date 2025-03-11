import requests

def get_football_data(endpoint, params=None):
    url = f"https://v3.football.api-sports.io/{endpoint}"
    headers = {
        "x-apisports-key": "800db00c1600661f9076b36f03350d8f"  # Ponha a sua chave de API
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if (response.status_code == 200):
        return response.json()
    else:
        return f"Erro: {response.status_code} - {response.text}"

def collect_raw_league_standings(league_id, start_season, end_season):
    raw_data = {}
    
    for year in range(start_season, end_season + 1):
        data = get_football_data("standings", {"league": league_id, "season": year})
        
        if("response" in data and data["response"]):
            raw_data[year] = data["response"]
    
    return raw_data

def save_standings_to_csv(standings, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Temporada","Posição", "Time", "Pontos", "Saldo de Gols", "Jogos", "Vitórias", "Empates", "Derrotas"])
            
        for season, data in standings.items():
            for league in data:
                for team in league['league']['standings'][0]:
                    writer.writerow([
                        season,
                        team["rank"],
                        team["team"]["name"],
                        team["points"],
                        team["goalsDiff"],
                        team["all"]["played"],
                        team["all"]["win"],
                        team["all"]["draw"],
                        team["all"]["lose"]
                        ])


def main():
    start_season = 2021
    end_season = 2023
    league_id = 71  # Brasileirão Série A
    
    raw_standings_data = collect_raw_league_standings(league_id, start_season, end_season)
    
    save_standings_to_csv(raw_standings_data, "brasileirao_standings.csv")

if (__name__ == "__main__"):
   main()
