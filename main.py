import nba
import streamlit as st
import pandas as pd

nba = nba.NbaStats()
title_arr = nba.get_title()
stats_arr = nba.get_player_stats()

all_time = nba.all_time_leaders()

