from art import logo

print(logo)

# Function to find the highest bidder
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidding_amount = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        if bid_amount > highest_bidding_amount:
            highest_bidding_amount = bid_amount
            winner = bidder
    print()
    print(f"The winner is {winner} with a bid of {highest_bidding_amount}")

# Dictionary to store bidder's name and bid_price as key and value pairs
bids = {}

continue_bidding = True
while  continue_bidding:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid?: $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    if should_continue == "yes":
        print("\n" * 50)
        



