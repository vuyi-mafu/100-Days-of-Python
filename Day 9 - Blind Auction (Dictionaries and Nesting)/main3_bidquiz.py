from art import logo

print(logo)
print("Welcome to the secret auction progam.")

continue_bid = True
bid_details = {}
bid_list = []

while continue_bid is True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bid_details[name] = bid
    # bid_list.append(bid_details)
    # bid_details = {}

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if more_bidders == "no":
        continue_bid = False

        max_value = max(bid_details.values())
        max_key = max(bid_details, key=bid_details.get)
        # print(bid_details)
        print(f"The winner is {max_key} with a bid of ${max_value}")

