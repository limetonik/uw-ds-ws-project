from urllib import request
from bs4 import BeautifulSoup as BS
import pandas as pd
import time

start_time = time.time() # To analyze the runtime

errors = []
matches = []

base_url = 'https://www.premierleague.com/match/'
start = 58898
for match in range(start,start+100): # Here we are limiting the code to go through 100 pages only
    try:
        url = f'https://www.premierleague.com/match/{match}'
        html = request.urlopen(url)
        bs = BS(html.read(), 'html.parser')

        home_team = bs.find_all('span', {'class': 'long'})[0].text
        away_team = bs.find_all('span', {'class': 'long'})[1].text
        scores = bs.find('div', {'class': 'score fullTime'}).text
        home_score = scores.split('-')[0] # Extracting home score from the "scores" string
        away_score = scores.split('-')[1] # Extracting away score from the "scores" string
        referee = bs.find('div', {'class': 'referee'}).text
        referee = referee.strip() # Getting rid of leading/trailing spaces
        stadium = bs.find('div', {'class': 'stadium'}).text
        stadium = stadium.strip() # Getting rid of leading/trailing spaces

    except:
        errors.append(match) # Appending match IDs to the errors list in case of any error
        continue

    match = [home_team, away_team, home_score, away_score, referee, stadium]
    matches.append(match)

columns = ['home_team', 'away_team', 'home_score', 'away_score', 'referee', 'stadium'] # Creating required columns
dataset = pd.DataFrame (matches, columns=columns) # Creating the dataframe
dataset.to_csv('Bs-PremierLeague_Matches.csv', index=False) # Exporting the dataset to .csv

# Looking into errors (if applicable)
print(f'Number of errors: {len(errors)}')
print('Errors:\n')
print(errors)

end_time = time.time() # To analyze the runtime
print(end_time - start_time)