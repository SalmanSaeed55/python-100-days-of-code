def find_highest_bidder(bid_dict):
    for bid in bid_dict:
        if bid_dict[bid] == max(bid_dict.values()):
            print(f"The winner is {bidder} with a bid of £{bids[bidder]}")


print("""
                         ___________
                         \\               /
                          )________(
                          |               |_.-._,.---------.,_.-.
                          |          | | |               | | ''-.    |
                          |          | | |_             _| |_..-' | 
                          |________| '-' `'---------'` '-'  
                          )               (
                         /_________\\
                         `'------------'`
                       .-------------.
                    /____________\\
""")

print("Welcome to the Blind Auction!")
bids = {}

more_people = "yes"
while more_people == "yes":
    bidder  = input("What is your name? \t")
    bid_amount = int(input("What is your bid? \t £"))

    bids[bidder] = bid_amount

    more_people = input("is there anyone else that would like to bid? \t")
    print("\n" * 100)

find_highest_bidder(bids)