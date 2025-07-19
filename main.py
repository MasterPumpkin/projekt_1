"""
main.py: první projekt do Engeto Online Python Akademie

author: Josef Nuhlíček
email: josef.nuhlicek@gmail.com
"""
import sys
from collections import Counter
from typing import List, Dict

# Kolekce textů určených k analýze
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

# Registrovaní uživatelé a jejich hesla
USERS = [
    {'username': 'bob', 'password': '123'},
    {'username': 'ann', 'password': 'pass123'},
    {'username': 'mike', 'password': 'password123'},
    {'username': 'liz', 'password': 'pass123'}
]

# Oddělovací čára pro výpis do konzole
SEPARATOR_LINE = '-' * 40

def login() -> bool:
    """
    Přihlásí uživatele na základě zadaného jména a hesla.

    Returns:
        bool: True pokud bylo přihlášení úspěšné, jinak False.
    """  
    username = input('Username: ')
    password = input('Password: ')
    for user in USERS:
        if (user['username'] == username and 
            user['password'] == password):
            print(SEPARATOR_LINE)
            print(f'Welcome to the app, {username}')
            print(f'We have {len(TEXTS)} texts to be analyzed.')
            print(SEPARATOR_LINE)
            return True
    return False


def split_text(text: str) -> List[str]:
    """
    Rozdělí text na slova podle mezer.
    
    Args:
        text (str): Vstupní text.
    
    Returns:
        List[str]: Seznam slov (řetězců).
    """
    return text.split()

def clean_words(words: List[str]) -> List[str]:
    """
    Odstraní z každého slova nežádoucí znaky.
    
    Args:
        words (List[str]): Seznam slov k pročištění.
    
    Returns:
        List[str]: Seznam pročištěných slov.
    """
    # Sada znaků, které budou odstraněny ze začátku a konce slov
    UNWANTED_CHARS = (
        '.,;:!?()[]{}"„“‚’«»<>@#$%^&*-_=+'
        '~/\\|`´'
    )
    return [
        cleaned
        for word in words
        if (cleaned := word.strip(UNWANTED_CHARS))
    ]

def categorize_words(words: List[str]) -> Dict[str, List[str]]:
    """
    Roztřídí slova do kategorií: titlecase, uppercase, lowercase, digit.
    Pokud slovo nezapadá do žádné z těchto kategorií, nezatřídí ho.
    
    Args:
        words (List[str]): Seznam pročištěných slov.
    
    Returns:
        Dict[str, List[str]]: Slovník kategorií a odpovídajících slov.
    """
    categories = {
        "titlecase": [],
        "uppercase": [],
        "lowercase": [],
        "digit": []
    }
    for word in words:
        if word.isdigit():
            categories["digit"].append(word)
        elif word.istitle():
            categories["titlecase"].append(word)
        elif word.isupper():
            categories["uppercase"].append(word)
        elif word.islower():
            categories["lowercase"].append(word)
    return categories

def count_word_lengths(words: List[str]) -> Counter:
    """
    Spočítá četnost délek slov.
    
    Args:
        words (List[str]): Seznam slov.
    
    Returns:
        Counter: Množství slov podle jejich délky.
    """
    return Counter(len(word) for word in words)

def sum_of_numbers(digit_words: List[str]) -> int:
    """
    Sečte číselné hodnoty všech slov, která obsahují pouze číslice.
    
    Args:
        digit_words (List[str]): Seznam číselných řetězců.
    
    Returns:
        int: Celkový součet všech čísel.
    """
    return sum(int(word) for word in digit_words)

def print_statistics(
    cleaned: List[str], 
    categories: Dict[str, List[str]], 
    word_lengths: Counter, 
    total_digits: int
) -> None:
    """
    Vytiskne statistiky o vstupním textu.
    
    Args:
        cleaned (List[str]): Očištěná slova.
        categories (Dict[str, List[str]]): Slovník slov podle kategorií.
        word_lengths (Counter): Četnosti délek slov.
        total_digits (int): Součet všech číselných řetězců.
    """
    print(SEPARATOR_LINE)
    print(f'There are {len(cleaned)} words in the selected text.')
    print(f'There are {len(categories["titlecase"])} titlecase words.')
    print(f'There are {len(categories["uppercase"])} uppercase words.')
    print(f'There are {len(categories["lowercase"])} lowercase words.')
    print(f'There are {len(categories["digit"])} numeric strings.')
    print(f'The sum of all the numbers {total_digits}')
    print(SEPARATOR_LINE)
    print('LEN|  OCCURRENCES       |NR.')
    print(SEPARATOR_LINE)
    for key, value in sorted(word_lengths.items()):
        print(f'{key:>3}|{"*" * value:<20}|{value:>2}')

def analyze(text: str) -> None:
    """
    Hlavní funkce, která zpracuje text a vypíše analýzu.
    
    Args:
        text (str): Vstupní text.
    """
    words = split_text(text)
    cleaned = clean_words(words)
    categories = categorize_words(cleaned)
    word_lengths = count_word_lengths(cleaned)
    total_digits = sum_of_numbers(categories["digit"])
    print_statistics(cleaned, categories, word_lengths, total_digits)


if __name__ == '__main__':
    if login():
        # Dotaz se dynamicky přizpůsobí počtu textů
        prompt = f'Enter a number btw. 1 and {len(TEXTS)} to select: '
        text_number_str = input(prompt).strip()

        try:
            text_number = int(text_number_str)
        except ValueError:
            sys.exit('You did not enter a number, terminating the program..')

        if 1 <= text_number <= len(TEXTS):
            # Změna pořadí: uživatel zadává 1 - 3, ale indexujeme od 0
            analyze(TEXTS[text_number - 1])
        else:
            sys.exit('Invalid number, terminating the program..')
    else:
        sys.exit('Unregistered user, terminating the program..')