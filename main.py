from machine import MENU, resources
from art import art

print(art, "\n"*2)

def insert_money(): # Function to repeat inserting money
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.10
    nickles = int(input("How many nickles?: "))*0.05
    pennies = int(input("How many pennies?: "))*0.01
    total_money = quarters+dimes+nickles+pennies
    return total_money

user_money = 0 # Storing your money from the inputs
while True:
    user_input = input("What would you like? (espresso/latte/capuccino): ").lower() # Ask user what to do
    if user_input == 'off': # Turning off the machine
        break
    elif user_input == 'report': # Look for the resources available in the machine
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
    elif user_input in MENU: 
        # Check if the resources if enough
        if resources['water'] < MENU[f'{user_input}']['ingredients']['water']: 
            print("Sorry there is not enough water in the machine")
        elif 'milk' in MENU[f'{user_input}']['ingredients'] and resources['milk'] < MENU[f'{user_input}']['ingredients']['milk']:
            print("Sorry there is not enough milk in the machine")
        elif resources['coffee'] < MENU[f'{user_input}']['ingredients']['coffee']:
            print("Sorry there is not enough coffee in the machine")
        else:
            # If enough resources, user started to input money
            user_money += insert_money()
            # Check user money
            if user_money < MENU[f'{user_input}']['cost']:
                print("Sorry, you don't have enough money to make coffee. Money Refunded")
                user_money -= user_money
            elif user_money >= MENU[f'{user_input}']['cost']:
                user_money -= MENU[f'{user_input}']['cost']
                resources['water'] -= MENU[f'{user_input}']['ingredients']['water']
                # Check if the milk is availbale in the menu, except for the Espresso
                if 'milk' in MENU[f'{user_input}']['ingredients']:
                    resources['milk'] -= MENU[f'{user_input}']['ingredients']['milk']
                resources['coffee'] -= MENU[f'{user_input}']['ingredients']['coffee']
                # Check if user insert too much money in the machine
                if user_money != 0:
                    print(f"Here is ${round(user_money, 3)} dollars in change.")
                    user_money -= user_money
                print(f"Here's your {user_input}. Enjoy!")