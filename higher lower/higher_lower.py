import random
import game_data


def show_person_details(letter, person):
    print(f"Compare {letter}: {person["name"]} a {person["description"]} from {person["country"]}.")


game_over = False
score = 0

while not game_over:

    # pick 2 remote people
    random_indices = random.sample(range(len(game_data.data)), 2)
    person_a = game_data.data[random_indices[0]]
    person_b = game_data.data[random_indices[1]]

    if person_a["follower_count"] > person_b["follower_count"]:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

    print('-----------------------------------------------------')
    show_person_details('A', person_a)
    print("vs.")
    show_person_details('B', person_b)

    waiting_for_answer = True
    while waiting_for_answer:
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}")
            waiting_for_answer = False
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
            waiting_for_answer = False
