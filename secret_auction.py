print('Welcome to the silent auction!')

all_bids = {}

next_user = 'yes'

#collect all bids
while next_user == 'yes':
    name = input('what is your name? ')
    bid = input('What is your bid? $')
    all_bids[name] = bid
    next_user = input('Is there another user? ')

#variables for the winner and their bid
highest = 0
winner = ''

#compare all bids and return the winner with highest bid
for bid in all_bids:
    bid_amount = all_bids[bid]
    if(int(bid_amount) > int(highest)):
        highest = bid_amount
        winner = bid

print('the winner is ' + winner + ' with a bid of ' + highest)