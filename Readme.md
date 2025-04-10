# Insights do Brasileirão

## Integrantes:
Matias Monteiro de Araújo

Dennynson Scheydt Medeiros do Nascimento

Vinícius da Silva Cunha

João Matheus Silva Paiva

**Descrição do Conjunto de Dados**
O conjunto de dados coletado contém informações sobre a classificação final do Campeonato Brasileiro Série A entre os anos de 2006 e 2024. Ele reúne estatísticas essenciais de cada temporada, permitindo análises sobre o desempenho dos times ao longo dos anos. O formato escolhido para armazenar os dados foi CSV, facilitando sua manipulação e integração com ferramentas de análise de dados.

**Processo de Coleta dos Dados**
A obtenção dos dados foi realizada em duas etapas principais. Primeiramente, utilizamos as API`s APIFootball e Football-data para coletar as informações referentes aos anos de 2021 a 2023. Posteriormente, para obter os dados das temporadas anteriores, empregamos web scraping utilizando as bibliotecas BeautifulSoup, requests, csv e re. O site utilizado para o scraping de dados foi WorldFootball.

**Descrição das Colunas**
- **Temporada**: Ano correspondente à edição do campeonato. Exemplo: `2019`
- **Posição**: Colocação final do time na tabela de classificação. Exemplo: `1`
- **Time**: Nome do clube participante. Exemplo: `Flamengo RJ`
- **Pontos**: Total de pontos conquistados na temporada. Exemplo: `90`
- **Saldo de Gols**: Diferença entre gols marcados e gols sofridos. Exemplo: `49`
- **Jogos**: Número de partidas disputadas na temporada. Exemplo: `38`
- **Vitórias**: Número total de vitórias na temporada. Exemplo: `28`
- **Empates**: Número total de empates na temporada. Exemplo: `6`
- **Derrotas**: Número total de derrotas na temporada. Exemplo: `4`
- **Gols Marcados**: Quantidade total de gols feitos pelo time. Exemplo: `86`
- **Gols Sofridos**: Quantidade total de gols sofridos pelo time. Exemplo: `37`

**Acesso aos Dados**
Os dados foram organizados e armazenados em um arquivo CSV, que está disponibilizado em uma pasta do Google Drive. Link: https://drive.google.com/file/d/1-zqg4gn4h_4_c1jHHLJF5A4SAmV1SuR3/view?usp=drive_link
