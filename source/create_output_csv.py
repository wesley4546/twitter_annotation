import csv

"""
The purpose of this function is:

1. Create a output_csv file equipped with the column_names

"""


def create_output_csv(file_name):
    # Column names of CSV
    csv_column_names = ['twitter_username',
                        'screen_name',
                        'date_joined',
                        'location',
                        'description',
                        'profile_photo',
                        'cover_photo',
                        'num_following',
                        'num_followers',
                        'num_tweets_replies',
                        'num_media',
                        'num_likes',
                        'num_topics',
                        'num_lists',
                        'type_of_account',
                        'spam',
                        'final_code',
                        'analysis',
                        'notes']


    # Writes CSV
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_column_names)
