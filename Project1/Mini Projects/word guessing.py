import random
word_list = ['ardvark', 'baboon', 'camel','apple']
word = list(random.choice(word_list))
print(word)

display = []
for e in range(len(word)):
    display.append('_')
print(display)

while '_' in display:
    guess = input('Guess a letter:').lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter
    print(display)

# another way of finding index and replace
# ind = 0
# for i in word:
#     if guess == i:
#         print('Right')
#         display[ind] = i
#     else:
#         print('Wrong')
#     ind += 1


