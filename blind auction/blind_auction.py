# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {}


def find_highest_bid():
    highest_bid = 0
    highest_bidder = ''
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            highest_bidder = bidder
    return highest_bidder


while True:
    print("\n" * 20)
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    next_bid = input("Is there another bid? (Y/N)").upper()
    if next_bid == 'N':
        break

print(find_highest_bid())
print('or...')
max_bidder = max(bids, key=bids.get)
print(f"The highest bidder is {max_bidder} with a bid of ${bids[max_bidder]}")

