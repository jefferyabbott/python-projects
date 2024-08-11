import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

game_is_playing = True
is_in_round = True


def deal_card():
    """Deal a random card from the deck."""
    return random.choice(cards)


def get_value_of_cards(hand):
    """Adds the value of all the cards in the hand."""
    total = sum(hand)
    if 11 in hand and total > 21:
        total -= 10
    return total


def get_hand_as_string(hand, show_last):
    """Displays the cards of a player.
    Takes a hand and boolean show_last.
    If show_last is False, use X for the last card"""
    if show_last:
        output = " ".join(map(str, hand))
        return output
    else:
        output = " ".join(map(str, hand[:-1]))
        return output + ' X'


while game_is_playing:
    # first deal
    player_cards.append(deal_card())
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
    dealer_cards.append(deal_card())

    # get totals
    player_score = get_value_of_cards(player_cards)
    dealer_score = get_value_of_cards(dealer_cards)

    if player_score >= 21:
        is_in_round = False

    while is_in_round:
        print(get_hand_as_string(player_cards, True))
        print(get_hand_as_string(dealer_cards, False))

        next_move = input("(H)it or (P)ass? ").upper()

        if next_move == 'H':
            player_cards.append(deal_card())
            dealer_cards.append(deal_card())
            player_score = get_value_of_cards(player_cards)
            dealer_score = get_value_of_cards(dealer_cards)
            if player_score >= 21:
                is_in_round = False
        elif next_move == 'P':
            is_in_round = False

    print(f"PLAYER RESULTS: {get_hand_as_string(player_cards, True)} = {player_score}")
    print(f"DEALER RESULTS: {get_hand_as_string(dealer_cards, True)} = {dealer_score}")

    if player_score == dealer_score:
        print("DRAW!")
    elif player_score == 21:
        print("YOU WIN!")
    elif dealer_score == 21:
        print("DEALER WINS!")
    elif player_score > 21 and dealer_score > 21:
        print("DRAW")
    elif player_score < 21 and dealer_score > 21:
        print("YOU WIN!")
    elif player_score < 21 and player_score > dealer_score:
        print("YOU WIN!")
    else:
        print("DEALER WINS!")

    play_again = input("Would you like to play again? (Y/N) ").upper()
    if play_again == 'Y':
        game_is_playing = True
        player_cards = []
        dealer_cards = []
        is_in_round = True
    else:
        game_is_playing = False
