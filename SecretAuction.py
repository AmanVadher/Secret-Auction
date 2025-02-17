import os
import art
print(art.logo)
bid_compare={}
count=True

def find_hightest_bidder(bidding_record):
    # {"aman":200,"jey":32}
    high=0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>high:
            high=bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${high}")
            

while count:
    name = input("What is your name : ")
    bid = int(input("Enter bid prize : $"))
    bid_compare[name]=bid
    next = input("Any bidder available? yes or no : ").lower()
    if next=="no":
        count=False
        os.system("cls")
        find_hightest_bidder(bid_compare)
    elif next=="yes":
        os.system("cls")
    else:
        print("Enter valid input")
