import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = (data.to_dict())
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your word: ")

name = name.upper()

letter_in_name = [letter for letter in name]

nato_phonetics = []
for letter in letter_in_name:
    nato_phonetics.append(alphabet_dict[letter])

print(nato_phonetics)


