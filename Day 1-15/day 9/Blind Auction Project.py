####### My Solution ########

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

# import art
# print(art.logo)

# # bits = {name: bit}
# bits = {}

# should_continue = True
# while should_continue:
#     name = input("what is you name: ")
#     bit = int(input("what amount is you bit: "))

#     bits[name] = bit

#     repeat = input("is there someone else? Type 'y' or 'n'. ").lower()
#     if repeat == "n":
#         should_continue = False
#     elif repeat == "y":
#         print("\n" * 20)
#     else:
#         print("invalid input")
#         should_continue = False

# # TODO-4: Compare bids in dictionary

# max = 0
# winner = ""
# for key in bits:
#     if bits[key] > max:
#         max = bits[key]
#         winner = key

# print(f"\n{"#"*20}\nthe winner is {winner}, ${max}")



####### Angila Solution ########
import art
print(art.logo)


# TODO-4: Compare bids in dictionary
def highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"\n{"#"*20}\nthe winner is {winner}, ${max}")


# bids = {name: bid}
bids = {}

should_continue = True
while should_continue:
    # TODO-1: Ask the user for input
    name = input("what is you name: ")
    bid = int(input("what amount is you bid: "))

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid

    # TODO-3: Whether if new bids need to be added
    repeat = input("is there someone else? Type 'y' or 'n'. ").lower()
    if repeat == "n":
        should_continue = False
        highest_bidder(bids)
    elif repeat == "y":
        print("\n" * 20)
    else:
        print("invalid input")
        should_continue = False


my_dict = {}
while True:
    key = input("Enter key (or press Enter to finish): ")
    if not key:  # Check if the input is empty (user pressed Enter)
        break
    value = input(f"Enter value for {key}: ")
    my_dict[key] = value
print(my_dict)