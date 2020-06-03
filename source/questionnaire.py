
"""
The purpose of this script is:

1. To create a 'Responses' class that will allow for easily storing responses
2. Create a dictionary of questions
3. Have a program that will ask the questions and return the answers in a 'Responses' class

"""


class Responses:

    def __init__(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13):
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


questions = {
    'question_1': '(TEXT) Enter Screen Name (Not the @ one): ',
    'question_2': '(BINARY) Is the account relevant for US? 1 or 0 ',
    'question_3': '(BINARY) Does the name include "bot" anywhere? 1 or 0 ',
    'question_4': '(BINARY) Are there emoticons in the name? 1 or 0 ',
    'question_5': '(BINARY) Are there emoticons in the profile description? 1 or 0 ',
    'question_6': '(TEXT) Describe the profile image briefly: ',
    'question_7': '(BINARY) Is the User Location sensible? Does it make sense? 1 or 0 ',
    'question_8': '(CATEGORY) What type of activity is found?\n'
                  'Tweeting - 1\n'
                  'Retweeting - 2\n'
                  'Replying - 3\n'
                  'Tweeting and Retweeting - 4\n'
                  'All (Tweeting, Retweeting, and Replying) - 5\n'
                  'Answer: ',
    'question_9': '(BINARY) Are the tweets multi-topical or uni-topical? 1 or 0 ',
    'question_10': '(TEXT) Write any notes that you have about the account. If none, put none ',
    'question_11': '(CATEGORY) Please code the following \n'
                   'Bot - 1 \n'
                   'Human - 2 \n'
                   'Hyprid - 3 \n'
                   'Impossible - 4\n'
                   'Answer: ',
    'question_12': '(TEXT) Please describe why you chose 4: ',
    'question_13': '(TEXT) **VERY IMPORTANT** Enter twitter username (The @ one): '
}


def questionnaire():
    ## INPUT ##

    separators = "----------------------"

    twitter_user_name = input(questions['question_13'])
    screen_name = input(questions['question_1'])
    print(separators)

    us_relevance = int(input(questions['question_2']))
    print(separators)

    if us_relevance != 0:

        name_bot = input(questions['question_3'])
        print(separators)

        name_emoji = input(questions['question_4'])
        print(separators)

        profile_emoji = input(questions['question_5'])
        print(separators)

        profile_image = input(questions['question_6'])
        print(separators)

        profile_location = input(questions['question_7'])
        print(separators)

        way_of_communication = input(questions['question_8'])
        print(separators)

        print("Sometimes, accounts post about more than one idea. For example, a tweet about sports, politics, "
              "entertainment.")
        content_diversity = input(questions['question_9'])

        notes = input(questions['question_10'])
        print(separators)

        final_code = int(input(questions['question_11']))

        if final_code == 4:
            reason_four = input(questions['question_12'])
        else:
            reason_four = "NA"
    else:
        name_bot = "NA"
        name_emoji = "NA"
        profile_emoji = "NA"
        profile_image = "NA"
        profile_location = "NA"
        way_of_communication = "NA"
        content_diversity = "NA"
        notes = "NA"
        final_code = "NA"
        reason_four = "NA"

    ## OUTPUT ##

    out = Responses(
        q1=screen_name,
        q2=us_relevance,
        q3=name_bot,
        q4=name_emoji,
        q5=profile_emoji,
        q6=profile_image,
        q7=profile_location,
        q8=way_of_communication,
        q9=content_diversity,
        q10=notes,
        q11=final_code,
        q12=reason_four,
        q13=twitter_user_name
    )

    return out
