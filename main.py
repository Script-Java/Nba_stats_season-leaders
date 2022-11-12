from bs4 import BeautifulSoup
import streamlit as st
import requests
import pandas as pd
import numpy as np


class NbaStats:
    def __init__(self):
        url = "https://www.nba.com/stats/players"
        response = requests.get(url)
        self.soup = BeautifulSoup(response.content, "html.parser")

    def get_title(self):
        header_list = []
        card_container = self.soup.find("div", {
            "class": "MaxWidthContainer_mwc__ID5AG LeaderBoard_leaderBoardContainer__2m0HJ"})
        for card in card_container:
            title = card.find("h2", {"class": "LeaderBoardCard_lbcTitleLink__MXurG"})
            if title is None:
                continue
            else:
                header_list.append(title.string)
        for card in card_container:
            title2 = card.find("h2", {"class": "LeaderBoardCard_lbcTitle___WI9J"})
            if title2 is None:
                continue
            else:
                header_list.append(title2.string)

        return header_list

    def get_player_stats(self):
        player_stats = []
        card_container = self.soup.find("div", {
            "class": "MaxWidthContainer_mwc__ID5AG LeaderBoard_leaderBoardContainer__2m0HJ"})
        for cards in card_container:
            table_body = cards.find("tbody")
            for stats in table_body:
                player_name = stats.find("a", {
                    "class": "Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL"}).string
                player_team = stats.find("span", {"class": "LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3"}).string
                player_stat = stats.find("td", {"class": "text-right lg:text-sm xl:text-base"}).string
                array = [player_name,player_team,player_stat]
                player_stats.append(array)
        return player_stats


# nba = NbaStats()
# df = pd.DataFrame(nba.get_player_stats(), columns=nba.get_title())
# st.write(df)
