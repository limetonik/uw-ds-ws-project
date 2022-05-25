from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from time import sleep

start_time = time.time() # To analyze the runtime

errors = []
matches = []

# Establising connection and generating URLs
option = Options()
option.headless = True # Value 'True' means that browser will not be  visible during execution of the code
driver = webdriver.Chrome(options=option,service=Service(ChromeDriverManager().install()))
driver.maximize_window() # This allows to maximize the browser window - it reduces the chances of Selenium script missing out on web elements they must interact with

start = 58898
for match in range(start,start+100): # Here we are limiting the code to go through 100 pages only
    my_url = f'https://www.premierleague.com/match/{match}'
    driver.get(my_url)
    sleep(5)
# Scraping the required data
    try:
        home_team = driver.find_element(By.XPATH, '//div[@class="team home"]').text
        away_team = driver.find_element(By.XPATH, '//div[@class="team away"]').text
        scores = driver.find_element(By.XPATH, '//div[@class="score fullTime"]').text
        home_score = scores.split('-')[0] # Extracting home score from the "scores" string
        away_score = scores.split('-')[1] # Extracting away score from the "scores" string
        referee = driver.find_element(By.XPATH, '//div[@class="referee"]').text
        stadium = driver.find_element(By.XPATH, '//div[@class="stadium"]').text
        time.sleep(1)

    except:
        driver.quit()
        errors.append(match) # Appending match IDs to the errors list in case of any error
        continue

    match = [home_team, away_team, home_score, away_score, referee, stadium]
    matches.append(match)

driver.quit()

# Exporting the data

columns = ['home_team', 'away_team', 'home_score', 'away_score', 'referee', 'stadium'] # Creating required columns
dataset = pd.DataFrame (matches, columns=columns) # Creating the dataframe
dataset.to_csv('Sl-PremierLeague_Matches.csv', index=False) # Exporting the dataset to .csv

# Looking into errors (if applicable)
print(f'Number of errors: {len(errors)}')
print('Errors:\n')
print(errors)

end_time = time.time() # To analyze the runtime
print(end_time - start_time)
