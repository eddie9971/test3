import pandas as pd

data = pd.read_csv('nato.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    name = input('Enter a name:').upper()
    try:
        new = [phonetic_dict[letter] for letter in name]
    except KeyError:
        print('Sorry, only letters in the alphabet.')
        generate_phonetic()
    else:
        print(new)


generate_phonetic()