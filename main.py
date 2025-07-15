"""
main.py: první projekt do Engeto Online Python Akademie

author: Josef Nuhlíček
email: josef.nuhlicek@gmail.com
"""
import sys

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = [
    {'username': 'bob', 'password': '123'},
    {'username': 'ann', 'password': 'pass123'},
    {'username': 'mike', 'password': 'password123'},
    {'username': 'liz', 'password': 'pass123'}
]

line = '-' * 40

def login():
    username = input('Username:')
    password = input('Password:')
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(line)
            print(f'Welcome to the app, {username}')
            print('We have 3 texts to be analyzed.')
            print(line)
            return True
    return False


def analyze(text):
    words = text.split()
    cleaned_words = []
    for word in words:
        clean_word = word.strip('.,')
        if clean_word:
            cleaned_words.append(clean_word)
    
    titlecase_words = []
    uppercase_words = []
    lowercase_words = []
    digit_words = []
    word_lengths = {}
    
    for word in cleaned_words:
        if word.istitle():
            titlecase_words.append(word)
        if word.isupper():
            uppercase_words.append(word)
        if word.islower():
            lowercase_words.append(word)
        if word.isdigit():
            digit_words.append(word)

        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1

    sum_of_digits = 0
    for word in digit_words:
        sum_of_digits = sum_of_digits + int(word)

    print(line)
    print(f'There are {len(cleaned_words)} words in the selected text.')
    print(f'There are {len(titlecase_words)} titlecase words.')
    print(f'There are {len(uppercase_words)} uppercase words.')
    print(f'There are {len(lowercase_words)} lowercase words.')
    print(f'There are {len(digit_words)} numeric strings.')
    print(f'The sum of all the numbers {sum_of_digits}')
    print(line)
    print('LEN|  OCCURRENCES  |NR.')
    print(line)

    for key, value in sorted(word_lengths.items()):
        print(f'{key:>3}|{"*" * value:<20}|{value:>2}')



if __name__ == '__main__':
    if login():
        text_number = input('Enter a number btw. 1 and 3 to select: ')
        if text_number.isdigit():
            text_number = int(text_number)
            if text_number >= 1 and text_number <= 3:
                analyze(TEXTS[text_number - 1])
            else:
                sys.exit('Invalid number, terminating the program..')
        else:
            sys.exit('You did not enter a number, terminating the program..')
    else:
        sys.exit('unregistered user, terminating the program..')