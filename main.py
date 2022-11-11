from bs4 import BeautifulSoup
import requests
import pandas as pd
from header import header_list
import streamlit as st
import time
import numpy as np


class Nba_stats:
    def __init__(self):
        url = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo" \
              "=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location" \
              "=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0" \
              "&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2022-23&SeasonSegment=&SeasonType=Regular" \
              "%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight= "

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'x-nba-stats-token': 'true',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'x-nba-stats-origin': 'stats',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://stats.nba.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        self.request = requests.get(url, headers=headers).json()

    def player_stats(self):
        player_stats = self.request["resultSets"][0]["rowSet"]
        data = pd.DataFrame(player_stats, columns=header_list)
        return data


nba = Nba_stats()
print(nba.player_stats())
