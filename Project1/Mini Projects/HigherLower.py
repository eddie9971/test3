import random
score = 0
should_continue = True

data = {
    'Taylor' : 314847,
    'Kobe': 392812,
    'James':394821,
    'MJ': 3920120,
    'JayC': 100000,
    'Apple':291938,
    'Wine':291038,
    'Whiskey':128930,
    'Music':129384
}


def check(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


while should_continue:
    a = random.choice(list(data))
    b = random.choice(list(data))
    while a == b:
        b = random.choice(list(data))

    guess = input('Who has more views, Type a or b: ').lower()

    is_correct = check(guess,data[a],data[b])
    if is_correct:
        score += 1
        print(f'You are right! Score: {score}')
    else:
        print(f'Wrong! Score:{score}')
        should_continue = False
    print(is_correct)