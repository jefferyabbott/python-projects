import sys
from morse_code import code as morse_code

def convert_to_morse_code(word):
    word = word.lower()
    code = []
    for char in word:
        if char in morse_code:
            code.append(morse_code[char])
    return code

for arg in sys.argv[1:]:
    print(f"{arg}: {convert_to_morse_code(arg)}")

