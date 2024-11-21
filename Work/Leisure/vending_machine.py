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


def vend(money, spent):
    print("Vending...")
    time.sleep(2)
    change = float(spent) - float(money)
    if change == 0.00:
        print("Thank you! ^.^")
    else:
        print("Please take your change...")
        print(f"Change: {change}")
    # return change


def selection_option(spent):
    selection = input("Please select an item...")

    match selection:
        case "A1":
            name = "Nacho Cheese Doritos"
            price = 1.00
            vend(price, spent)
        case "A1":
            name = "Nacho Cheese Doritos"
            price = 1.00
            vend(price, spent)
        case "A2":
            name = "Nacho Cheese Doritos"
            price = 1.00
            vend(price, spent)
        case "A3":
            name = "Nacho Cheese Doritos"
            price = 1.00
            vend(price, spent)
        case "A4":
            name = "Nacho Cheese Doritos"
            price = 1.00
            vend(price, spent)
        case "A5":
            name = "Nacho Cheese Doritos"
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

    selection_option(collected)


collect_money()





