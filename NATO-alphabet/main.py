import pandas as pd

nato_phonetic_alphabets = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetics_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabets.iterrows()}


user_input = input("Enter a word:\n")
code_word = [nato_phonetics_dict[letter.upper()] for letter in user_input]
print(code_word)
