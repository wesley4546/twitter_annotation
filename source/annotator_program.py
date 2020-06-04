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
    # Messaging
    separators = "----------------------"
    print("Twitter Bot Qualitative Coding")
    print(separators)

    # This checks to make sure that it's either reading the raw CSV or the output from the check_duplicate function
    try:
        annotationcsv = pd.read_csv(input_annotation_file)
        cleanedcsv = annotationcsv.dropna(how='all', subset=['ScreenName']).to_dict()
        URLS = cleanedcsv['URL']
    except:
        annotationcsv = input_annotation_file.to_dict()
        URLS = annotationcsv['URL']

    # Starts loop to append to CSV
    for url in URLS:
        # Opens the twitter URL
        webbrowser.open(URLS[url])

        # Starts the questionnaire
        annotation = questionnaire()

        # Creates the rows to append
        csv_file_rows = (
            annotation.q13,
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
        )

        # Appends the CSV file
        with open(output_file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_file_rows)
