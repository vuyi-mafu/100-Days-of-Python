MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


on = True
money = 0


def check_resources(water, milk, coffee, choice, cost):
    """Function to check if the resources are available to make a cup of coffee. Updates the resources dictionary if
    the resources are sufficient."""
    resource_water = resources["water"]
    resource_coffee = resources["coffee"]
    resource_milk = resources["milk"]
    global money
    money += cost
    if (resource_water >= water) and (resource_coffee >= coffee) and (resource_milk >= milk):
        resource_water -= water
        resource_coffee -= coffee
        resource_milk -= milk
        resources["water"] = resource_water
        resources["milk"] = resource_milk
        resources["coffee"] = resource_coffee
        calculate_cost(cost, choice)
    elif (resource_water < water) and (resource_coffee >= coffee) and (resource_milk >= milk):
        print("Sorry there is not enough water.")
    elif (resource_water >= water) and (resource_coffee < coffee) and (resource_milk >= milk):
        print("Sorry there is not enough coffee.")
    elif (resource_water >= water) and (resource_coffee >= coffee) and (resource_milk < milk):
        print("Sorry there is not enough milk.")
    elif (resource_water >= water) and (resource_coffee < coffee) and (resource_milk >= milk):
        print("Sorry there is not enough coffee.")
    elif (resource_water >= water) and (resource_coffee < coffee) and (resource_milk < milk):
        print("Sorry there is not enough coffee and milk.")
    elif (resource_water < water) and (resource_coffee < coffee) and (resource_milk >= milk):
        print("Sorry there is not enough water and coffee.")
    # elif choice == "report":
    #     print(f"Water: {resource_water}")
    #     print(f"Milk: {resource_milk}")
    #     print(f"Coffee: {resource_coffee}")
    #     print(f"Water: {resource_water}")
    else:
        print("There is not enough resources")


def calculate_cost(cost, choice):
    """Function to calculate the total amount in coins inserted into the machine and the change owed to the person."""
    print("Please insert coins.")
    num_of_quarters = int(input("how many quarters?: "))
    num_of_dimes = int(input("how many dimes?: "))
    num_of_nickles = int(input("how many nickles?: "))
    num_of_pennies = int(input("how many pennies?: "))
    quarters = num_of_quarters * 0.25
    dimes = num_of_dimes * 0.1
    nickles = num_of_nickles * 0.05
    pennies = num_of_pennies * 0.01
    total_cost = quarters + dimes + nickles + pennies
    # print(f"The total cost for the coffee is ${total_cost}")
    if cost > total_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif total_cost > cost:
        change = total_cost - cost
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}. Enjoy!")
    elif choice == "report":
        print("Money!!")


def make_coffee():
    """Function to make a cup of coffee. Extracts the ingredients required to make each type of coffee."""
    global on, money
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        milk = 0
        cost = MENU["espresso"]["cost"]
        check_resources(water, milk, coffee, choice, cost)
    elif choice == "latte":
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        cost = MENU["latte"]["cost"]
        check_resources(water, milk, coffee, choice, cost)
    elif choice == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        cost = MENU["cappuccino"]["cost"]
        check_resources(water, milk, coffee, choice, cost)
    elif choice == "off":
        on = False
    elif choice == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")


while on:
    make_coffee()



