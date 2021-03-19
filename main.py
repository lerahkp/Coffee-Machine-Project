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
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

PENNY = 0.01
DIME = 0.10
NICKEL = 0.05
QUARTER = 0.25
profit=0
money=0


def sufficient_resource(resources,MENU):
  if drink == "espresso" and resources["Water"] < MENU["espresso"]["ingredients"]["water"]:
    print("Sorry there is not enough water")
    return False
  elif drink == "espresso" and resources["Coffee"] <  MENU["espresso"]["ingredients"]["coffee"]:
    print("Sorry there is not enough Coffee")
    return False
  elif drink == "latte" and resources["Water"] <  MENU["latte"]["ingredients"]["water"]:
    print("Sorry there is not enough water")
    return False
  elif drink == "latte" and resources["Coffee"] <  MENU["latte"]["ingredients"]["coffee"]:
    print("Sorry there is not enough Coffee")
    return False
  elif drink == "latte" and resources["Milk"] <  MENU["latte"]["ingredients"]["milk"]:
    print("Sorry there is not enough milk")
    return False
  elif drink == "cappuccino" and resources["Water"] <  MENU["cappuccino"]["ingredients"]["water"]:
    print("Sorry there is not enough water")
    return False
  elif drink == "cappuccino" and resources["Coffee"] <  MENU["cappuccino"]["ingredients"]["coffee"]:
    print("Sorry there is not enough Coffee")
    return False
  elif drink == "cappuccino" and resources["Milk"] <  MENU["cappuccino"]["ingredients"]["milk"]:
    print("Sorry there is not enough milk")
    return False
  else:
    return True

def coin_process():
  global money
  print("please enter coins")
  quarters = int(input("how many quarters: "))
  dimes = int(input("how many dimes: "))
  nickels = int(input("how many nickels: "))
  pennies = int(input("how many pennies: "))
  money = quarters*QUARTER + dimes * DIME + pennies*PENNY + nickels * NICKEL

def check_tranasction_success(MENU,resources):
  global profit
  if drink == "espresso" and money < MENU["espresso"]["cost"]:
    print("Sorry that's not enough Money. Money refunded")
  elif drink == "latte" and money < MENU["latte"]["cost"]:
    print("Sorry that's not enough money. Money refunded")  
  elif drink == "cappuccino" and money < MENU["cappuccino"]["cost"]:
    print("Sorry that's not enough money. Money refunded")
  elif drink == "espresso" and money >= MENU["espresso"]["cost"]:
    resources["Water"] = resources["Water"] - MENU["espresso"]["ingredients"]["water"]
    resources["Coffee"] = resources["Coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    excess = round(money - MENU["espresso"]["cost"],2)
    print(f"Here is your ${excess} in change.")
    print('Here is your espresso  ☕  Enjoy!')
    profit += 1.5
  elif drink == "latte" and money >= MENU["latte"]["cost"]:
    resources["Water"] = resources["Water"] - MENU["latte"]["ingredients"]["water"]
    resources["Coffee"] = resources["Coffee"] - MENU["latte"]["ingredients"]["coffee"]
    resources["Milk"] = resources["Milk"] - MENU["latte"]["ingredients"]["milk"]
    excess = round(money - MENU["latte"]["cost"],2)
    print(f"Here is your ${excess} in change.")
    print('Here is your latte ☕ Enjoy!')
    profit += 2.5
  elif drink == "cappuccino" and money >= MENU["cappuccino"]["cost"]:
    resources["Water"] = resources["Water"] - MENU["cappuccino"]["ingredients"]["water"]
    resources["Coffee"] = resources["Coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
    resources["Milk"] = resources["Milk"] - MENU["cappuccino"]["ingredients"]["milk"]
    excess = round(money - MENU["cappuccino"]["cost"],2)
    print(f"Here is your ${excess} in change.")
    print('Here is your cappuccino ☕ Enjoy!')
    profit += 3
  else:
    print("error in input")

continue_game = True
while continue_game:
  drink = input("What would you like? (espresso, latte, cappuccino): ").lower()
  if drink == "espresso" or drink == "latte" or drink == "cappuccino":
    if sufficient_resource(resources,MENU):
       coin_process()
       check_tranasction_success(MENU,resources)
  elif drink == "report":
    print(f"Water: {resources['Water']}ml")
    print(f"Milk: {resources['Milk']}ml")
    print(f"Coffee: {resources['Coffee']}g")
    print(f"Money: ${profit}")
  elif drink == "off":
    continue_game=False
  else:
    print("key error")
    continue_game=False

