# etl/get_ctp_data.py - ETL module for EST framework.
__version__ = '0.1'
__all__ = ['ctp_url', 'keep_cols']

#import dash
#import dash_table
import pandas as pd
from etl import *
from etl.etl import *
from lib.utils import *

ctp_url = 'https://covidtracking.com/api/v1/states/daily'
df = get_ctp_state_historic() # legacy etl functon, should be class

keep_cols = ['date', 'state', 'positive', 'hospitalized', 'death']
df = keep_df_cols(df, keep_cols)

states = list(df.state.unique()) # np arr is faster
df.sort_values('date', axis=0, ascending=True, inplace=True, kind='quicksort', na_position='last')

parse_state_daily_data(df) # split all states dataframe into a dataframe for each each state and write to fs
                
