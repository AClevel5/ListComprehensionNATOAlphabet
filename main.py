import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
program_complete = False

while not program_complete :
    try:
        name = input("What is your name?").upper()
        letters = [n for n in name]
        nato_pronunciation = [nato_dict[letter] for letter in letters]
        print(nato_pronunciation)
    except KeyError:
        print("Please only enter valid letters of the alphabet.")
    else:
        program_complete = True
