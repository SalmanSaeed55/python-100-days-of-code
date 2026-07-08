import pandas as pd

nato_alph = pd.read_csv("./nato_phonetic_alphabet.csv")
df = pd.DataFrame(nato_alph)

nato_alph_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word you would like to spell out using the NATO alphabet: ").upper()

word_phonetics = [nato_alph_dict.get(letter) for letter in word]
print(word_phonetics)