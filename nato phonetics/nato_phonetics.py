import pandas

# read NATO phonetic code words from csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_words = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    phonetic_list = [phonetic_words[letter] for letter in word]
    print(phonetic_list)
    go_again = input("\nGo again? (Y/N) ").upper()
    if go_again == 'N':
        break
