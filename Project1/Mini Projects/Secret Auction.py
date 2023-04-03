
all_bid = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for name in bidding_record:
        bid = bidding_record[name]
        if bid > highest_bid:
            highest_bid = bid
            winner = name
    print(f'The winner is {winner} with a bid of ${highest_bid}')


while not bidding_finished:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: '))
    all_bid[name] = bid
    more = input('Are there any other bidders? Type yes or no: ').lower()
    if more == 'no':
        bidding_finished = True
        find_highest_bidder(all_bid)
    else:
        continue


