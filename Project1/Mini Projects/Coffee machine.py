MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'milk': 0,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

for coffee in MENU:
    print(coffee)

for i in MENU.values():
    print(i['ingredients'])
    print(i['cost'])


def pay(choice,q,d,n,p):
    payment = q*0.25+d*0.1+n*0.05+p+0.01
    coffee_cost = MENU[choice]['cost']
    if payment > coffee_cost:
        change = payment-coffee_cost
        print(f'Here is ${change} in change')
    elif payment < coffee_cost:
        shortage = coffee_cost - payment
        print(f'The item cost ${coffee_cost}, you still need ${shortage}')
    else:
        print('Here is your coffee')
    return payment


def use_resource(choice):
    global enough
    coffee_ingredients = MENU[choice]['ingredients']
    if choice in MENU.keys():
        for source in resources:
            resources[source] -= coffee_ingredients[source]
            if resources[source] <= 0:
                print(f'not enough {source}')
                enough = False
    else:
        print('We don\'t have that item')


if __name__ == '__main__':
    enough = True
    while enough:
        coffee_choice = input('What would you like? (espresso, latte, cappuccino): ')
        if coffee_choice == 'report':
            print(resources)
        else:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickles = int(input('How many nickles?: '))
            pennies = int(input('How many pennies?: '))
            total_payment =pay(coffee_choice,quarters,dimes,nickles,pennies)
            use_resource(coffee_choice)






