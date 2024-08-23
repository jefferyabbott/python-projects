import pandas

# read NATO phonetic code words from csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_words = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_words[letter] for letter in word]
        print(phonetic_list)
    except KeyError as error_message:
        print(f"Please enter letters only, {error_message} is not valid.")
    go_again = input("\nGo again? (Y/N) ").upper()
    if go_again == 'N':
        break
