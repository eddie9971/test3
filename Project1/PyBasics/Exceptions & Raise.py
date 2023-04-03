try:
    file = open('aaa.txt')
    a_dictonary = {'key': 'value'}
    print(a_dictonary['key'])
except FileNotFoundError:
    print('there is no such file')
except KeyError as error_message:
    print(f'The key {error_message} does not exist.')
except NameError:
    print('file does not exist')
else:
    content = file.read()
    print(content)
finally:
    print('File was closed')

h = float(input('Height: '))
w = float(input('Weight: '))


if h > 3:
    raise ValueError('Human Height should not be over 3 meters')
bmi = w / h ** 2
print(bmi)

fruits = ['Orange', 'Apple', 'Banana']


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit Pie')
    else:
        print(fruit + 'Pie')


facebook_posts = [
    {'Likes': 10 , 'Comments': 10, 'Shares': 4},
    {'Likes': 10 , 'Comments': 10, 'Shares': 4},
    {'Comments': 10, 'Shares': 4},
    {'Likes': 10 , 'Comments': 10, 'Shares': 4},
    {'Likes': 10 , 'Comments': 10, 'Shares': 4},
]


def total_likes():
    likes = 0
    for post in facebook_posts:
        try:
            likes = likes + post['Likes']
        except KeyError:
            likes += 0
    return likes


print(total_likes())