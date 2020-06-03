import pandas as pd

"""
The purpose of this function is:

1. Act sort of like a "save" function. What it does is find out what twitter usernames were done, and makes sure to 
   skip them. 

"""


def check_for_duplicates(annotation_csv, output_csv):
    # Removes NAs
    ant_csv = pd.read_csv(annotation_csv).dropna(how='all', subset=['ScreenName'])
    out_csv = pd.read_csv(output_csv).dropna(how='all', subset=['screen_name'])

    # Gets the usernames that already are done
    out_csv_usernames = out_csv['twitter_username'].to_list()

    # Removes them from the csv
    consolidated_csv = ant_csv[~ant_csv['ScreenName'].isin(out_csv_usernames)]

    return consolidated_csv
