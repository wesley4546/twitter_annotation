from os import path
from source.create_output_csv import create_output_csv
from source.annotator_program import annotator_program
from source.check_for_duplicates import check_for_duplicates
from source.print_welcome_message import print_welcome_message

"""
This is the main program that stitches it all together.

1. It checks to make sure an output file isn't already created (if it is, it creates one)
2. If there is one, it makes sure to pick up where it left off

"""

# This is where you input what your annotations file is called, and what you want the output file to be called
input_file_name = "annotation_Wesley.csv"  # This one has the list of your twitter usernames and URLs
output_file_name = "twitter_annotations.csv"  # This is the name of the file the program will create

print_welcome_message()

if not path.exists(output_file_name):
    print("Creating output CSV...")
    create_output_csv(output_file_name)
    annotator_program(input_file_name, output_file_name)
else:
    print("Picking up where you left off...")
    consolidated_csv = check_for_duplicates(input_file_name, output_file_name)
    annotator_program(consolidated_csv, output_file_name)
