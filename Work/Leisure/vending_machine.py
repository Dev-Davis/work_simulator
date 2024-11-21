import time
import sys

# if money not inserted, display price for item

# if money is and `collected` money is not >= item amount, display message

# if it is, vend item, and give change if needed

# add credit card feature in future


print("1 - Insert $1")
print("5 - Insert 5 cents")
print("10 - Insert 10 cents")
print("25 - Insert 25 cents")
print("")


def vending_items():
    print("A1 - Nacho Cheese Doritos")
    time.sleep(0.1)
    print("A2 - Lays Salt and Vinegar")
    time.sleep(0.1)
    print("A3 - Cooler Ranch Doritos")
    time.sleep(0.1)
    print("A4 - Flamin Hot Popcorn")
    time.sleep(0.1)
    print("A5 - Smartfood White Cheddar Popcorn")
    time.sleep(0.1)
    print("*******************************")
    time.sleep(0.1)
    print("B1 - Nerds Gummy Ropes")
    time.sleep(0.1)
    print("B2 - Trail Mix")
    time.sleep(0.1)
    print("B3 - Skittles")
    time.sleep(0.1)
    print("B4 - Oreo")
    time.sleep(0.1)
    print("B5 - 3 Musketeers")
    time.sleep(0.1)
    print("*******************************")
    time.sleep(0.1)
    print("C1 - Reese's")
    time.sleep(0.1)
    print("C2 - Kit Kat")
    time.sleep(0.1)
    print("C3 - Twix")
    time.sleep(0.1)
    print("C4 - Snickers")
    time.sleep(0.1)
    print("C5 - Pop Tarts")
    time.sleep(0.1)
    print("*******************************")
    time.sleep(0.1)
    print("")
    time.sleep(2)

def vend(money, spent):
    print("Vending...")
    change = float(spent) - float(money)
    if change == 0.00:
        print("Thank you! ^.^")
    else:
        print("Please take your change...")
        print(f"Change: {change}")
    # return change


def selection_option(spent):
    selection = input("Please select an item...")

    time.sleep(2)
    match selection:
        case "A1":
            name = "Nacho Cheese Doritos"
            price = 1.00
            vend(price, spent)
        case "A2":
            name = "Lays Salt and Vinegar"
            price = 1.00
            vend(price, spent)
        case "A3":
            name = "Cooler Ranch Doritos"
            price = 1.00
            vend(price, spent)
        case "A4":
            name = "Flamin Hot Popcorn"
            price = 1.00
            vend(price, spent)
        case "A5":
            name = "Smartfood White Cheddar Popcorn"
            price = 1.00
            vend(price, spent)
        case "B1":
            name = "Nerds Gummy Ropes"
            price = 1.00
            vend(price, spent)
        case "B2":
            name = "Trail Mix"
            price = 1.00
            vend(price, spent)
        case "B3":
            name = "Skittles"
            price = 1.00
            vend(price, spent)
        case "B4":
            name = "Oreo"
            price = 1.00
            vend(price, spent)
        case "B5":
            name = "3 Musketeers"
            price = 1.00
            vend(price, spent)
        case "C1":
            name = "Reese's"
            price = 1.00
            vend(price, spent)
        case "C2":
            name = "Kit Kat"
            price = 1.00
            vend(price, spent)
        case "C3":
            name = "Twix"
            price = 1.00
            vend(price, spent)
        case "C4":
            name = "Snickers"
            price = 1.00
            vend(price, spent)
        case "C5":
            name = "Pop Tarts"
            price = 1.00
            vend(price, spent)


def collect_money():
    collected = 0.00

    print("Insert money...")
    print("*Type amount above to insert change*")

    while collected < 1.00:
        spent = int(input(f"Money: {collected} \n"))
        time.sleep(0.3)
        match int(spent):
            case 1:
                collected = collected + 1.00
            case 5:
                collected = collected + 0.05
            case 10:
                collected = collected + 0.10
            case 25:
                collected = collected + 0.25
            case _:
                print("Please insert $1 or correct change")

    vending_items()
    selection_option(collected)


collect_money()





