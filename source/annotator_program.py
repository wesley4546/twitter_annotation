import webbrowser
import pandas as pd
import csv
from source.questionnaire import questionnaire

"""
This function is made to take in the annotation_(name).csv file and a output file name then do the following:

 1. Open the twitter user
 2. Start the questionnaire
 3. Append the output annotation file

"""


def annotator_program(input_annotation_file, output_file_name):

    # This checks to make sure that it's either reading the raw CSV or the output from the check_duplicate function
    try:
        annotationcsv = pd.read_csv(input_annotation_file)
        cleanedcsv = annotationcsv.dropna(how='all', subset=['ScreenName']).to_dict()
        URLS = cleanedcsv['URL']
        screen_names = cleanedcsv['ScreenName']
    except:
        annotationcsv = input_annotation_file.to_dict()
        URLS = annotationcsv['URL']
        screen_names = annotationcsv['ScreenName']

    # Starts loop to append to CSV
    for url in URLS:
        # Tells the User
        print("\nStarting annotation for user:", screen_names[url])

        # Opens the twitter URL
        webbrowser.open(URLS[url])

        # Starts the questionnaire
        annotation = questionnaire()

        # Creates the rows to append
        csv_file_rows = (
            screen_names[url],
            annotation.q1,
            annotation.q2,
            annotation.q3,
            annotation.q4,
            annotation.q5,
            annotation.q6,
            annotation.q7,
            annotation.q8,
            annotation.q9,
            annotation.q10,
            annotation.q11,
            annotation.q12,
            annotation.q13,
            annotation.q14,
            annotation.q15,
            annotation.q16,
            annotation.q17,
            annotation.q18,
            annotation.q19,
            annotation.q20,
            annotation.q21,
            annotation.q22,
            annotation.q23,
            annotation.q24
        )

        # Appends the CSV file
        with open(output_file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_file_rows)

    print("Done!")