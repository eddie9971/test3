# creating card values

cards = {
    'Ace': 11,
    'King': 10,
    'Queen': 10,
    'Jack': 10,
    'Ten': 10,
    'Nine': 9,
    'Eight': 8,
    'Seven': 7,
    'Six': 6,
    'Five': 5,
    'Four': 4,
    'Three': 3,
    'Two': 2
}



# creating a deck of cards

deck = []

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

for suit in suits:
    for card, value in cards.items():
        deck.append(f"{card} of {suit}")



# Blackjack Game

# Creating the Deck
import random

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] * 4
cards_value = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10,
               "Queen": 10, "King": 10}


# betting system
def bet():
    while True:
        try:
            global stake
            stake = int(input("Welcome, what is your stake? "))
        except:
            print("Please enter an integer")
            continue
        else:
            if stake > 0:
                print(f"Stake enterred: ${stake}")
                break
            else:
                print("Please enter a valid stake. ")


# deals cards to player and dealer
def deal_cards():
    global player_hand, dealer_hand, player_score, dealer_score


player_hand = []
dealer_hand = []

random.shuffle(cards)

player_hand.append(cards.pop())
dealer_hand.append(cards.pop())

player_hand.append(cards.pop())
dealer_hand.append(cards.pop())

player_score = sum([cards_value[i] for i in player_hand])
dealer_score = sum([cards_value[i] for i in dealer_hand])

print(f"Player has {player_hand}      (score: {player_score})")
print(f"Dealer has {dealer_hand}      (score: {dealer_score})")


# game status
def game_status():
    global player_score, dealer_score, stake


    if player_score == 21 and dealer_score != 21:
        print("Blackjack! Congratulations")
        stake = stake * 2.5
        print(f"You won {stake}")
        return True
    elif dealer_score == 21 and player_score != 21:
        print("Dealer has Blackjack! You lose!")
        stake = 0
        return True
    elif dealer_score > 21:
        print("Dealer has busted! You win!")
        stake = stake * 2
        print(f"You won {stake}")
        return True
    elif player_score > 21:
        print("You have busted! You lose!")
        stake = 0
        return True
    elif dealer_score >= 17 and dealer_score > player_score and dealer_score < 21:
        print("Dealer has won!")
        stake = 0
        return True
    elif player_score > dealer_score and player_score < 21:
        return False
    elif dealer_score > player_score and dealer_score < 21:
        return False
    elif player_score == dealer_score:
        print("It's a tie!")
        stake = stake
        return True


# player choice to hit or stand
def take_card():
    global player_score, player_hand


    new_card = cards.pop()
    player_hand.append(new_card)
    player_score += cards_value[new_card]
    print(f"You have drawn {new_card} (Score: {player_score})")
    if game_status() == True:
        return True


def ask_question():
    while True:
        answer = input("Do you want to take another card? (Y/N)")


    if answer.upper() == "Y":
        return False
    elif answer.upper() == "N":
        return True
    else:
        print("Invalid input. Please try again.")
        continue


# main game
def main_game():
    global stake


while True:
    bet()
    deal_cards()
    while True:
        if take_card() == True:
            break
        if ask_question() == True:
            break
    while True:
        if game_status() == True:
            break
        elif dealer_score >= 17:
            break
        else:
            dealer_hand.append(cards.pop())
            dealer_score = sum([cards_value[i] for i in dealer_hand])

    print(f"Dealer's hand is {dealer_hand} (Score: {dealer_score})")
    play_again = input("Do you want to play again? (Y/N)")
    if play_again.upper() == "Y":
        stake = stake
        continue
    elif play_again.upper() == "N":
        print("Thanks for playing, bye!")
        break

# Execute game
main_game()