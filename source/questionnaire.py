from source.input_validation_functions import *

"""
The purpose of this script is:

1. To create a 'Responses' class that will allow for easily storing responses
2. Create a dictionary of questions
3. Have a program that will ask the questions and return the answers in a 'Responses' class

"""


class Responses:

    def __init__(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12,
                 q13, q14, q15, q16, q17, q18):
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


questions = {
    'question_1': '1. (TEXT) Copy and Paste the name of account (Not the @ one): ',
    'question_2': '2. (TEXT) Enter date join (Format = ‘month, year’): ',
    'question_3': '3. (TEXT) Enter user location (If none, put ‘NA’): ',
    'question_4': '4. (BINARY) Does the account have a description? (1 or 0): ',
    'question_5': '5. (BINARY) Does the account have a profile photo? (1 or 0): ',
    'question_6': '6. (BINARY) Does the account have a cover photo? (1 or 0): ',
    'question_7': '7. (NUMERIC) Enter number of accounts the account is following: ',
    'question_8': '8. (NUMERIC) Enter number of accounts following this account: ',
    'question_9': '9. (NUMERIC) Enter number of tweets and replies displayed: ',
    'question_10': '10. (NUMERIC) Enter number of media displayed: ',
    'question_11': '11. (NUMERIC) Enter number of posts liked by the account: ',
    'question_12': '12. (NUMERIC) Enter number of topics the account follows:',
    'question_13': '13. (NUMERIC) Enter number of lists the account belongs to: ',
    'question_14': '14. (CATEGORY) Is this an Individual or Organization account?\n'
                   'Individual - 1\n'
                   'Organization - 2\n'
                   'Answer: ',
    'question_15': '15: (BINARY) Is this a spamming account? (1 or 0): ',
    'question_16': '16. (CATEGORY) Please code the account as following:\n'
                   'Bot - 1\n'
                   'Hybrid - 2\n'
                   'Non-bot; Genuine - 3\n'
                   'Impossible to decide - 4\n'
                   'Answer: ',
    'question_17': '17. (TEXT) Please enter analysis: ',
    'question_18': '18. (TEXT) Please enter any notes about this account (If none, put `NA`)'
}


def questionnaire():
    ## INPUT ##

    separators = "\n-------------------------------------------------------------\n"
    # Text
    # screen_name = validate_text_response(questions['question_1'])

    # Text
    name_of_user = validate_text_response(questions['question_1'])
    print(separators)

    # Text
    date_joined = validate_text_response(questions['question_2'])
    print(separators)

    # Text
    location = validate_text_response(questions['question_3'])
    print(separators)

    # Binary
    description = validate_binary_response(questions['question_4'])
    print(separators)

    # Binary
    profile_photo = validate_binary_response(questions['question_5'])
    print(separators)

    # Binary
    cover_photo = validate_binary_response(questions['question_6'])
    print(separators)

    # Numeric
    num_following = validate_numeric_response(questions['question_7'])
    print(separators)

    # Numeric
    num_followers = validate_numeric_response(questions['question_8'])
    print(separators)

    # Numeric
    num_tweets_replies = validate_numeric_response(questions['question_9'])
    print(separators)

    # Numeric
    num_media = validate_numeric_response(questions['question_10'])
    print(separators)

    # Numeric
    num_likes = validate_numeric_response(questions['question_11'])
    print(separators)

    # Numeric
    num_topics = validate_numeric_response(questions['question_12'])
    print(separators)

    # Numeric
    num_lists = validate_numeric_response(questions['question_13'])
    print(separators)

    # Category
    type_of_account = validate_category_response(questions['question_14'], 2)
    print(separators)

    # Binary
    spam = validate_binary_response(questions['question_15'])
    print(separators)

    # Category
    final_code = validate_category_response(questions['question_16'], 4)
    print(separators)

    # Text
    analysis = validate_text_response(questions['question_17'])
    print(separators)

    # Text
    notes = validate_text_response(questions['question_18'])

    ## OUTPUT ##

    out = Responses(
        q1=name_of_user,
        q2=date_joined,
        q3=location,
        q4=description,
        q5=profile_photo,
        q6=cover_photo,
        q7=num_following,
        q8=num_followers,
        q9=num_tweets_replies,
        q10=num_media,
        q11=num_likes,
        q12=num_topics,
        q13=num_lists,
        q14=type_of_account,
        q15=spam,
        q16=final_code,
        q17=analysis,
        q18=notes
    )

    return out
