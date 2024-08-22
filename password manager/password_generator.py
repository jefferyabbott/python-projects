from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=', ']', '[']

def generate_random_password():
    number_of_letters = randint(5, 8)
    number_of_numbers = randint(2, 3)
    number_of_special_characters = randint(2, 3)

    password_list = []

    for i in range(number_of_letters):
        if i % 2 == 0:
            password_list.append(choice(letters))
        else:
            password_list.append(choice(letters).upper())

    random_numbers = [choice(numbers) for _ in range(number_of_numbers)]
    random_special_characters = [choice(special_characters) for _ in range(number_of_special_characters)]

    password_list = password_list + random_numbers + random_special_characters

    shuffle(password_list)
    return ''.join(password_list)