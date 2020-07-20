from source.input_validation_functions import *

"""
The purpose of this script is:

1. To create a 'Responses' class that will allow for easily storing responses
2. Create a dictionary of questions
3. Have a program that will ask the questions and return the answers in a 'Responses' class

"""


class Responses:

    def __init__(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12,
                 q13, q14, q15, q16, q17, q18, q19, q20):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16
        self.q17 = q17
        self.q18 = q18
        self.q19 = q19
        self.q20 = q20


questions = {
    'question_1': '1. (BINARY) Are 7 or more out of the 10 most recent tweets/retweets in English? (0 = No, 1 = Yes) ',
    'question_2': '2. (TEXT) Copy and Paste the name of account (Do not include the @ name): ',
    'question_3': '3. (TEXT) Enter date joined (Format = ‘month year’; for example, ‘may 2020’): ',
    'question_4': '4. (TEXT) Enter the account location (If none, put ‘NA’; for example, ‘Tampa Florida‘): ',
    'question_5': '5. (BINARY) Does the account have a description? (0 = No, 1 = Yes): ',
    'question_6': '6. (BINARY) Does the account have a profile photo? (0 = No, 1 = Yes): ',
    'question_7': '7. (BINARY) Does the account have a cover photo? (0 = No, 1 = Yes): ',
    'question_8': '8. (NUMERIC) Enter number of accounts the account is following: ',
    'question_9': '9. (NUMERIC) Enter number of accounts following the account: ',
    'question_10': '10. (NUMERIC) Enter number of tweets and replies displayed: ',
    'question_11': '11. (NUMERIC) Enter number of media displayed: ',
    'question_12': '12. (NUMERIC) Enter number of posts liked by the account: ',
    'question_13': '13. (NUMERIC) Enter number of topics the account follows: ',
    'question_14': '14. (NUMERIC) Enter number of lists the account belongs to: ',
    'question_15': '15. (BINARY) Is this an Official Institutional account? (0 = No, 1 = Yes): ',
    'question_16': '16: (BINARY) Is this a spamming account? (0 = No, 1 = Yes): ',
    'question_17': '17. (CATEGORY) Is this account a bot or hybrid or human being?\n'
                   'Bot - 1\n'
                   'Hybrid - 2\n'
                   'Human Being - 3\n'
                   'Impossible to decide - 4\n'
                   'Answer: ',
    'question_18': '18. (TEXT) ANALYSIS - What does the account try to achieve topically or socially or politically? ',
    'question_19': '19. (TEXT) Please enter any notes about this account (If none, put `NA`): ',
    'question_20': '20. (NUMERIC) Please enter number of minutes it took to complete investigation: '
}


def questionnaire():
    ## INPUT ##

    separators = "\n-------------------------------------------------------------\n"

    # Binary
    english = validate_binary_response(questions['question_1'])
    print(separators)

    if english == "1":
        # Text
        name_of_user = validate_text_response(questions['question_2'])
        print(separators)

        # Text
        date_joined = validate_text_response(questions['question_3'])
        print(separators)

        # Text
        location = validate_text_response(questions['question_4'])
        print(separators)

        # Binary
        description = validate_binary_response(questions['question_5'])
        print(separators)

        # Binary
        profile_photo = validate_binary_response(questions['question_6'])
        print(separators)

        # Binary
        cover_photo = validate_binary_response(questions['question_7'])
        print(separators)

        # Numeric
        num_following = validate_numeric_response(questions['question_8'])
        print(separators)

        # Numeric
        num_followers = validate_numeric_response(questions['question_9'])
        print(separators)

        # Numeric
        num_tweets_replies = validate_numeric_response(questions['question_10'])
        print(separators)

        # Numeric
        num_media = validate_numeric_response(questions['question_11'])
        print(separators)

        # Numeric
        num_likes = validate_numeric_response(questions['question_12'])
        print(separators)

        # Numeric
        num_topics = validate_numeric_response(questions['question_13'])
        print(separators)

        # Numeric
        num_lists = validate_numeric_response(questions['question_14'])
        print(separators)

        # Category
        institutional = validate_binary_response(questions['question_15'])
        print(separators)

        # Binary
        spam = validate_binary_response(questions['question_16'])
        print(separators)

        # Category
        final_code = validate_category_response(questions['question_17'], 4)
        print(separators)

        # Text
        analysis = validate_text_response(questions['question_18'])
        print(separators)

        # Text
        notes = validate_text_response(questions['question_19'])

        # Numeric
        time = validate_numeric_response(questions['question_20'])
    else:
        name_of_user = "NA"
        date_joined = "NA"
        location = "NA"
        description = "NA"
        profile_photo = "NA"
        cover_photo = "NA"
        num_following = "NA"
        num_followers = "NA"
        num_tweets_replies = "NA"
        num_media = "NA"
        num_likes = "NA"
        num_topics = "NA"
        num_lists = "NA"
        institutional = "NA"
        spam = "NA"
        final_code = "NA"
        analysis = "NA"
        notes = "NA"
        time = "NA"


    ## OUTPUT ##

    out = Responses(
        q1=english,
        q2=name_of_user,
        q3=date_joined,
        q4=location,
        q5=description,
        q6=profile_photo,
        q7=cover_photo,
        q8=num_following,
        q9=num_followers,
        q10=num_tweets_replies,
        q11=num_media,
        q12=num_likes,
        q13=num_topics,
        q14=num_lists,
        q15=institutional,
        q16=spam,
        q17=final_code,
        q18=analysis,
        q19=notes,
        q20=time
    )

    return out
