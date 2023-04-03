import random
senarios = ['win', 'lose']
bet_result = random.choice(senarios)
cash = 3000
total_bets = []
count = 1
losing = True


try:
    bets = int(input('place your bet: \n$'))
    cash -= bets
    if bets > cash:
        print(f'You only have ${cash}, try smaller bet.')
    elif bets == 0:
        print('Bet can not be Zero')
    else:
        while losing:
            status = str(input(f'Did you win round #{count} ? Please Enter Yes or No:\n>>>').lower())
            if status == 'yes':
                losing == False
                total_bets.append(bets)
                cash += bets*2
                print(f'Congratulations! You have won ${total_bets[-1]} on your #{count} round, you now have ${cash}')
                break
            elif status == 'no':
                count += 1
                total_bets.append(bets)
                bets = sum(total_bets)*2
                if cash < bets:
                    print(
                        f'You don\'t have enough cash for next round!! You need ${bets} for next round. Your Cash '
                        f'Balance  = ${cash}')
                    break
                else:
                    cash -= bets
                    print(
                        f'You have lost last round, ${bets} are placed for next round, good luck on your #{count} '
                        f'round! (Cash Balance = ${cash})')
            else:
                print('Invalid Input, try again')
except ValueError:
    print('Please enter a valid number.')
except NameError:
    print('Please enter a valid number.')
