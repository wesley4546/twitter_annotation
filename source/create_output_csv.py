import csv

"""
The purpose of this function is:

1. Create a output_csv file equipped with the column_names

"""


def create_output_csv(file_name):
    # Column names of CSV
    csv_column_names = ['twitter_username',
                        'screen_name',
                        'relevance',
                        'name_include_bot',
                        'name_include_emoji',
                        'profile_include_emoji',
                        'profile_image_desc',
                        'user_location_sensible',
                        'communication_medium',
                        'content_diversity',
                        'notes',
                        'account_coding',
                        'reason_for_impossible']

    # Writes CSV
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_column_names)
