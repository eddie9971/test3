import random


def generate():
    num = random.randint(0,2)
    return _dict[num]


_dict = {
    0:'rock',
    1:'paper',
    2:'scissors'
}


# player = input(f'Rock, Paper, or Scissors?\n>>>').lower()
# computer = generate()

player_win_count = 0
computer_win_count = 0
total_count = 3
while total_count != 0:
    player = input(f'Rock, Paper, or Scissors?\n>>>').lower()
    computer = generate()
    total_count -= 1

    if player == computer:
        print(f"Tie! You chose {player} and the computer chose {computer}")
    elif player == "rock" and computer == "paper":
        print(f"Computer wins! You chose {player} and the computer chose {computer}")
        computer_win_count += 1
    elif player == "rock" and computer == "scissors":
        print(f"You win! You chose {player} and the computer chose {computer}")
        player_win_count += 1
    elif player == "paper" and computer == "rock":
        print(f"You win! You chose {player} and the computer chose {computer}")
        player_win_count += 1
    elif player == "paper" and computer == "scissors":
        print(f"Computer wins! You chose {player} and the computer chose {computer}")
        computer_win_count += 1
    elif player == "scissors" and computer == "rock":
        print(f"Computer wins! You chose {player} and the computer chose {computer}")
        computer_win_count += 1
    elif player == "scissors" and computer == "paper":
        print(f"You win! You chose {player} and the computer chose {computer}")
        player_win_count += 1

if player_win_count > computer_win_count:
    print('You have Won!')
elif player_win_count == computer_win_count:
    print('Tie!')
else:
    print('You Lost!')