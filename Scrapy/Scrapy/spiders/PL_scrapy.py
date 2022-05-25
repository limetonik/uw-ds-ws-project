# -*- coding: utf-8 -*-
import scrapy

class Match(scrapy.Item):
    home_team = scrapy.Field()
    away_team = scrapy.Field()
    referee = scrapy.Field()
    stadium = scrapy.Field()
    home_score = scrapy.Field()
    away_score = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'PL_Matches'
    allowed_domains = ['https://www.premierleague.com/']
    start = 58898
    try:
        start_urls = [f'https://www.premierleague.com/match/{id}'
                    for id in range(start,start+100)] # Here we are limiting the code to go through 100 pages only
    except:
        start_urls = []

    for url in start_urls:
        def parse(self, response):
            p = Match()
            home_team_xpath = '//*[@id="mainContent"]/div/section[2]/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]/text()'
            away_team_xpath = '//*[@id="mainContent"]/div/section[2]/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]/text()'
            scores_xpath = '//*[@id="mainContent"]/div/section[2]/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div/text()'
            referee_xpath = '//*[@id="mainContent"]/div/section[2]/div[2]/section/div[1]/div/div[1]/div[2]/text()'
            stadium_xpath = '//*[@id="mainContent"]/div/section[2]/div[2]/section/div[1]/div/div[1]/div[3]/text()'
            scores = response.xpath(scores_xpath).getall()
            home_score = ([i.split(',') for i in scores])[0] # Extracting home score from the "scores" string
            away_score = ([i.split(',') for i in scores])[1] # Extracting away score from the "scores" string
            p['home_team'] = response.xpath(home_team_xpath).getall()
            p['away_team'] = response.xpath(away_team_xpath).getall()
            referee = response.xpath(referee_xpath).getall()
            referee = [i.strip() for i in referee] # Getting rid of leading/trailing spaces
            referee = [i.replace(",","") for i in referee][1]
            p['referee'] = referee
            stadium = response.xpath(stadium_xpath).getall()
            stadium = [i.strip() for i in stadium] # Getting rid of leading/trailing spaces
            p['stadium'] = stadium
            p['home_score'] = home_score
            p['away_score'] = away_score

            yield p