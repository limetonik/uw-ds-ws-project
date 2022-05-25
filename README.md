# uw-ds-ws-project
Final Project for Web Scraping and Social Media Scraping Course (2022)

Project Objective
Web Scraping of Premier League fixture results. 

Target data points:
- Home team
- Away team
- Home score
- Away score
- Referee
- Stadium

The source domain is: https://www.premierleague.com/

**How to install?**
- BeautifulSoup: 
```
pip install beautifulsoup4
```
- Selenium: 
```
pip install selenium
```
- Scrapy: 
```
pip install Scrapy
```

**How to run the scrapers**

*BeautifulSoup*
```python

python soup/PL_soup.py
```

*Selenium*
```python
python selenium/PL_selenium.py
```

*Scrapy*
```python
scrapy crawl PL_Matches -o PL_Matches.csv
```
