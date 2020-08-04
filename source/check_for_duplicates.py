import pandas as pd

"""
The purpose of this function is:

1. Act sort of like a "save" function. What it does is find out what twitter usernames were done, and makes sure to 
   skip them. 

"""


def check_for_duplicates(annotation_csv, output_csv):
    try:
        # Removes NAs
        ant_csv = pd.read_csv(annotation_csv).dropna(how='all', subset=['ScreenName'])
    except:
        print("ERROR: Problem with column names of `input_csv`. Make sure the column names are `ScreenName` and `URL`")

    try:
        out_csv = pd.read_csv(output_csv)
    except:
        print("ERROR: Problem with reading `output_csv`.")

    # Gets the usernames that already are done
    out_csv_usernames = out_csv['twitter_username'].to_list()

    # Removes them from the csv
    consolidated_csv = ant_csv[~ant_csv['ScreenName'].isin(out_csv_usernames)]

    return consolidated_csv
