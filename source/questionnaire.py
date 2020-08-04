from source.input_validation_functions import *

"""
The purpose of this script is:

1. To create a 'Responses' class that will allow for easily storing responses
2. Create a dictionary of questions
3. Have a program that will ask the questions and return the answers in a 'Responses' class

"""


class Responses:

    def __init__(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12,
                 q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24):
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
        self.q21 = q21
        self.q22 = q22
        self.q23 = q23
        self.q24 = q24


questions = {
    'question_qualify': '(CATEGORY) Should this account be disqualified?\n'
                        '1 - Yes | Less than 7 total tweets\n'
                        '2 - Yes | Less than 7/10 most recent tweets in English\n'
                        '3 - Yes | Offensive (Pornographic, Gory, etc.)\n'
                        '4 - Yes | Impossible to code because the account is suspended, protected\n'
                        '5 - No  | Continue\n'
                        'Answer: ',
    'question_scrn_name': '(TEXT) Enter the screen name (use the bolded name above the @username, exclude emojis): ',
    'question_joined': '(TEXT) Enter date joined (Format = ‘month year’; for example, ‘may 2020’): ',
    'question_loc': '(TEXT) Enter the account location (If none, put ‘NA’; for example, ‘Tampa Florida‘): ',
    'question_desc': '(BINARY) Does the account have a description? (0 = No, 1 = Yes): ',
    'question_prof_photo': '(BINARY) Does the account have a profile photo? (0 = No, 1 = Yes): ',
    'question_cov_photo': '(BINARY) Does the account have a cover photo? (0 = No, 1 = Yes): ',
    'question_following': '(NUMERIC) Enter number of accounts the account is following: ',
    'question_follower': '(NUMERIC) Enter number of accounts following the account: ',
    'question_tweets_replies': '(NUMERIC) Enter number of tweets and replies displayed: ',
    'question_media': '(NUMERIC) Enter number of media displayed: ',
    'question_likes': '(NUMERIC) Enter number of posts liked by the account: ',
    'question_topics': '(NUMERIC) Enter number of topics the account follows: ',
    'question_lists': '(NUMERIC) Enter number of lists the account belongs to: ',
    'question_instit': '(BINARY) Is this an Official Institutional account? (0 = No, 1 = Yes): ',
    'question_spam': '(BINARY) Is this a spamming account? (0 = No, 1 = Yes): ',
    'question_code': '(CATEGORY) Is this account a bot or hybrid or human being?\n'
                     '1 - Bot\n'
                     '2 - Hybrid\n'
                     '3 - Human Being\n'
                     'Answer: ',
    'question_notes': '(TEXT) NOTES - Please include any miscellaneous notes '
                      '(e.g. mistakes during annotation, meta-commentary, suggestions, confusion during annotation).\n'
                      '(If none, put `NA`): ',
    'question_time': '(NUMERIC) Please enter number of minutes it took to complete investigation: ',
    'question_evidence': '(TEXT) EVIDENCE - Provide three lines of evidence defending your categorization: ',
    'question_num_analysis': '(NUMERIC) ANALYSIS - What is the purpose of this account? Select (up to three) relevant '
                             'purposes:\n'
                             '1 - Personal\n'
                             '2 - Entertainment\n'
                             '3 - Political\n'
                             '4 - Professional\n'
                             '5 - Marketing\n'
                             '6 - Information Aggregation\n'
                             '(for example, `34` means Political and Professional): ',
    'question_theme': '(TEXT) Additional Themes – Does this account have any purposes not covered in the previous '
                      'question?\n'
                      'If so, please explain. (If none, put NA): ',
    'question_confidence': '(CATEGORY) Please indicate your level of confidence that your assessment is correct\n'
                           '1 - <50% | Probably not accurate\n'
                           '2 -  50% | Could go either way\n'
                           '3 -  75% | Assessment is probably accurate\n'
                           '4 -  90% | Assessment is almost certainly accurate\n'
                           '5 -  99% | I’ll bet my first born this is right\n'
                           'Answer: '
                           '',
    'question_expl_conf': '(TEXT) Please explain the reasoning behind your confidence score: '

}


def questionnaire():
    ## INPUT ##

    separators = "\n-------------------------------------------------------------\n"
    question_number = 1

    # Binary
    print_question_number(question_number)
    qualify = validate_category_response(questions['question_qualify'], 5)
    question_number += 1

    if qualify == 5:

        # Text
        print_question_number(question_number)
        name_of_user = validate_text_response(questions['question_scrn_name'])
        question_number += 1

        # Text
        print_question_number(question_number)
        date_joined = validate_text_response(questions['question_joined'])
        question_number += 1

        # Text
        print_question_number(question_number)
        location = validate_text_response(questions['question_loc'])
        question_number += 1

        # Binary
        print_question_number(question_number)
        description = validate_binary_response(questions['question_desc'])
        question_number += 1

        # Binary
        print_question_number(question_number)
        profile_photo = validate_binary_response(questions['question_prof_photo'])
        question_number += 1

        # Binary
        print_question_number(question_number)
        cover_photo = validate_binary_response(questions['question_cov_photo'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_following = validate_numeric_response(questions['question_following'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_followers = validate_numeric_response(questions['question_follower'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_tweets_replies = validate_numeric_response(questions['question_tweets_replies'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_media = validate_numeric_response(questions['question_media'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_likes = validate_numeric_response(questions['question_likes'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_topics = validate_numeric_response(questions['question_topics'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_lists = validate_numeric_response(questions['question_lists'])
        question_number += 1

        # Category
        print_question_number(question_number)
        institutional = validate_binary_response(questions['question_instit'])
        question_number += 1

        # Binary
        print_question_number(question_number)
        spam = validate_binary_response(questions['question_spam'])
        question_number += 1

        # Category
        print_question_number(question_number)
        final_code = validate_category_response(questions['question_code'], 3)
        question_number += 1

        # Text
        print_question_number(question_number)
        evidence = validate_text_response(questions['question_evidence'])
        question_number += 1

        # ?
        print_question_number(question_number)
        confidence = validate_category_response(questions['question_confidence'], 5)
        question_number += 1

        # Text
        print_question_number(question_number)
        expl_confidence = validate_text_response(questions['question_expl_conf'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        num_analysis = validate_numeric_response(questions['question_num_analysis'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        add_theme = validate_text_response(questions['question_theme'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        notes = validate_text_response(questions['question_notes'])
        question_number += 1

        # Numeric
        print_question_number(question_number)
        time = validate_numeric_response(questions['question_time'])
        question_number += 1


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
        evidence = "NA"
        num_analysis = "NA"
        add_theme = "NA"
        confidence = "NA"
        expl_confidence = "NA"
        notes = "NA"
        time = "NA"

    ## OUTPUT ##

    out = Responses(
        q1=qualify,
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
        q18=evidence,
        q19=confidence,
        q20=expl_confidence,
        q21=num_analysis,
        q22=add_theme,
        q23=notes,
        q24=time
    )

    return out


def print_question_number(question_number):
    separators = "-----------------------------"

    print(separators, question_number, separators)
