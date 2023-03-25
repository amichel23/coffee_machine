# Makes three hot flavors, expresso, latte, cappuccino

# Espresso - 50ml water, 18g Coffee (1.5)

# Latte 200ml water, 24g coffee, 150ml milk (2.5)

# cappuccino - 250ml water, 24g coffee,100ml milk (3)

# coin operated

# requirements 1. print report 2. check sufficient resources 3. process coins 4. check if transaction is successful
# 5. make coffee

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
        },
        'cost': 3
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

money = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, and false if there is not enough resources"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f'sorry there is not enough {i}')
            return False
    return True


def process_coins():
    """Returns total calculated from coins inserted"""
    print('Please insert coins.')
    QUARTER = .25
    DIME = .1
    NICKLE = .05
    PENNY = 0.01
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickels = int(input('How many nickels: '))
    pennies = int(input('How many pennies: '))
    total = round((quarters * QUARTER) + (dimes * DIME) + (nickels * NICKLE) + (pennies * PENNY), 2)
    return total


def is_transaction_sufficient(money_received, cost_of_drink):
    """return true if payment is accepted, false if there isn't enough money"""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕️')


is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'water: {resources["water"]}ml')
        print(f'coffee: {resources["coffee"]}g')
        print(f'milk: {resources["milk"]}ml')
        print(f'money: ${money}')
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_sufficient(payment, drink['cost']):
                make_coffee(choice,drink['ingredients'])








