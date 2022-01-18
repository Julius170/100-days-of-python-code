MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10,
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
    "coffee": 100.
}

your_order = input("what do you want: ")
for items in MENU:
    order_water = your_order["water"]
    order_milk = your_order["milk"]
    order_coffee = "cappuccino"["coffee"]
    print(order_water)
    print(order_milk)
    print(order_coffee)
if your_order != "cappuccino" or "cappuccino" !="milk" or "cappuccino" != "coffee":
    print("Invalid Input")
# TODO: 1. print a report of all the coffee's resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
print(f"water: {water}ml")
print(f"milk: {milk}ml")
print(f"coffee: {coffee}ml")
# print(f"money: {money}")


# TODO: 2. Check that the resource are sufficient to make the drink order?
if order_water < water or order_milk < milk or order_coffee < coffee:
    print("Insufficient Ingredients")

# TODO: 3. Process coins
payment = input("Pay for the drink: ")
# TODO: 4. Check transaction successful

# TODO: 5. Make Coffee
