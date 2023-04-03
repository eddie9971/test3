import random
from typing import List, Tuple, Any

card_values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ['♣', '♦', '♥', '♠']


face_cards = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A'
}

fc_vals = {
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': (1,11)
}


def generate_cards():
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = (face_cards[value], suit)
            else:
                _card = (value, suit)
            cards.append(_card)
    return  cards


cards = generate_cards()


def deal_card():
    index = random.randint(0,len(cards)-1)
    hit_card = cards.pop(index)
    return hit_card


def deal2():
    cards1 = deal_card()
    cards2 = deal_card()
    hand = [cards1,cards2]
    return hand


def get_hand_val(hand):
    val = 0
    for card in hand:
        if card[0] in fc_vals:
            if card[0] != 'A':
                val += fc_vals[card[0]]
            else:
                if val + fc_vals[card[0]][1] > 21:
                    val += fc_vals[card[0]][0]
                else:
                    val += fc_vals[card[0]][1]
        else:
            val += card[0]

    return val


def hit_me(hand):
    hit = deal_card()
    hand.append(hit)
    # new_hand_val = get_hand_val(hand)
    return hand


if __name__ == '__main__':

    my_hand = deal2()
    dealer_hand = deal2()
    # initial deal
    print(f'Your hand: {my_hand}')
    my_hand_val = get_hand_val(my_hand)
    print(my_hand_val)
    if my_hand_val == 21:
        print('Blackjack!')
        exit()
    print(f'Dealer hand: {dealer_hand[0]}')
    dealer_hand_val = get_hand_val(dealer_hand)
    if dealer_hand_val == 21:
        print('Dealer Blackjack!')
        exit()
    # hit or not
    hit_or_no_hit = input('Do you wish to hit? (Y/N)\t').lower()
    while hit_or_no_hit == 'y':
        my_hand = hit_me(my_hand)
        my_hand_val = get_hand_val(my_hand)
        print(my_hand)
        print(my_hand_val)
        if my_hand_val == 21:
            print('You win!')
            exit()
        elif my_hand_val > 21:
            print('You busted!')
            exit()
        hit_or_no_hit = input('Do you wish to hit? (Y/N)\t').lower()
    # handling the dealer hand
    print(f'Dealer han val: {dealer_hand_val}')
    while dealer_hand_val <= 16:
        dealer_hand = hit_me(dealer_hand)
        dealer_hand_val = get_hand_val(dealer_hand)
        print('Dealer hits')
        print(dealer_hand)
        print(f'Dealer hand val: {dealer_hand_val}')
        if dealer_hand_val == 21:
            print('Dealer wins :(')
            exit()
        elif dealer_hand_val > 21:
            print('Dealer busted!')
            exit()
    # comparing hand values
    if my_hand_val < 21 and dealer_hand_val < 21:
        if my_hand_val > dealer_hand_val:
            print('You win!')
        elif dealer_hand_val > my_hand_val:
            print('Dealer wins :(')
        else:
            print('Tie!')