from __future__ import division
from bs4 import BeautifulSoup
import requests
stats = []
def grabstats(game):
    html = requests.get(game).text
    soup = BeautifulSoup(html, 'html5lib')

    # GRAB ALL STAT INFO
    for td_tag in soup.find_all('td'):
        stat = td_tag.text
        stats.append(stat)
        
# Insert the website in which you would like to scrap
print(grabstats("http://www.espn.co.uk/nfl/matchup?gameId=400951612"))
stats = [x.replace('\t', '').replace('\n', '') for x in stats]
print(stats)
