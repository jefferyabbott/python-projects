alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, key, direction):
    """Encodes or decodes the text by shifting using the position of letters in the key."""
    output_text = ''
    key_position = 0
    for character in original_text:
        if character in alphabet:
            if key_position > len(key) - 1:
                key_position = 0
            shift_amount = alphabet.index(key[key_position])
            if direction == 'encode':
                index_of_encrypted_letter = (alphabet.index(character) + shift_amount) % len(alphabet)
            else:
                index_of_encrypted_letter = (alphabet.index(character) - shift_amount) % len(alphabet)
            output_text += alphabet[index_of_encrypted_letter]
            key_position += 1
        else:
            output_text += character
    print(f"Here is the encoded result: {output_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print('Please enter encode or decode!')
    else:
        text = input("Type your message:\n").lower()
        key = input("Enter the encryption key, example: TUK:\n").lower()
        encrypt(original_text=text, key=key, direction=direction)
        go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        if go_again == 'no':
            break
