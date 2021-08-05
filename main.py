import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")


df_dict = {row.letter: row.code for (index, row) in df.iterrows()}

print(df_dict)

user_input = input("Please enter a word:\n")

phonetic_list = [df_dict[word.capitalize()] for word in user_input]

print(phonetic_list)