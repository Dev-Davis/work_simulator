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
    snacks = {}

    print("***** Chips *****")
    print("A1 - Nacho Cheese Doritos - $1.75")
    # time.sleep(0.1)
    print("A2 - Lays Salt and Vinegar - $1.75")
    # time.sleep(0.1)
    print("A3 - Cooler Ranch Doritos - $1.75")
    # time.sleep(0.1)
    print("A4 - Flamin Hot Popcorn - $1.75")
    # time.sleep(0.1)
    print("A5 - Smartfood White Cheddar Popcorn - $1.75")
    print("")
    time.sleep(0.1)
    print("***** Candies *****")
    # time.sleep(0.1)
    print("B1 - Nerds Gummy Ropes - $1.50")
    # time.sleep(0.1)
    print("B2 - Trail Mix - $1.50")
    # time.sleep(0.1)
    print("B3 - Skittles - $1.20")
    # time.sleep(0.1)
    print("B4 - Oreo - $1.50")
    # time.sleep(0.1)
    print("B5 - Life Saver Gummies - $1.20")
    print("")
    time.sleep(0.1)
    print("***** Candy Bars *****")
    time.sleep(0.1)
    print("C1 - Reese's - $1.55")
    # time.sleep(0.1)
    print("C2 - Kit Kat - $1.55")
    # time.sleep(0.1)
    print("C3 - Twix - $1.55")
    # time.sleep(0.1)
    print("C4 - Snickers - $1.55")
    # time.sleep(0.1)
    print("C5 - Pop Tarts - $1.55")
    print("")
    time.sleep(0.1)
    print("*******************************")
    time.sleep(0.1)
    print("")
    time.sleep(0.2)


def needed_funds(remaining, spent):
    added = 0.00
    while added < remaining:
        spend = int(input(f"Insert money... \n"))
        time.sleep(0.3)
        match int(spend):
            case 1:
                added = added + 1.00
                print(f"{spent + added:.2f}")
            case 5:
                added = added + 0.05
                print(f"{spent + added:.2f}")
            case 10:
                added = added + 0.10
                print(f"{spent + added:.2f}")
            case 25:
                added = added + 0.25
                print(f"{spent + added:.2f}")
            case _:
                print("Please insert accepted change or bills...")

    return spent + added


def vend(price, spent, name):
    change = float(spent) - float(price)
    remaining = price - spent
    if change < 0.00:
        print(f"Not enough funds. Please insert {remaining:.2f}")
        total = needed_funds(remaining, spent)

    if remaining == 0.00:
        print(f"Vending {name}...")
        time.sleep(2)
        print("Thank you! ^.^")
    else:
        print(f"Vending {name}...")
        total_change = total - price

        if total_change == 0.00:
            print("Have a dope day! ^.^")
        else:
            time.sleep(2)
            print("Please collect snacks and change...")
            print(f"Change: {total_change:.2f}")
            print("Have a dope day! ^.^")


def selection_option(spent):
    selection = input("Please select an item... \n").capitalize()
    time.sleep(1)

    match selection:
        case "A1":
            name = "Nacho Cheese Doritos"
            price = 1.75
            vend(price, spent, name)
        case "A2":
            name = "Lays Salt and Vinegar"
            price = 1.75
            vend(price, spent, name)
        case "A3":
            name = "Cooler Ranch Doritos"
            price = 1.75
            vend(price, spent, name)
        case "A4":
            name = "Flamin' Hot Popcorn"
            price = 1.75
            vend(price, spent, name)
        case "A5":
            name = "Smartfood White Cheddar Popcorn"
            price = 1.75
            vend(price, spent, name)
        case "B1":
            name = "Nerds Gummy Ropes"
            price = 1.50
            vend(price, spent, name)
        case "B2":
            name = "Trail Mix"
            price = 1.50
            vend(price, spent, name)
        case "B3":
            name = "Skittles"
            price = 1.20
            vend(price, spent, name)
        case "B4":
            name = "Oreo"
            price = 1.50
            vend(price, spent, name)
        case "B5":
            name = "3 Musketeers"
            price = 1.20
            vend(price, spent, name)
        case "C1":
            name = "Reese's"
            price = 1.55
            vend(price, spent, name)
        case "C2":
            name = "Kit Kat"
            price = 1.55
            vend(price, spent, name)
        case "C3":
            name = "Twix"
            price = 1.55
            vend(price, spent, name)
        case "C4":
            name = "Snickers"
            price = 1.55
            vend(price, spent, name)
        case "C5":
            name = "Pop Tarts"
            price = 1.55
            vend(price, spent, name)
        case _:
            print("Please make a valid selection...")

    return price


def collect_money():
    collected = 0.00
    # print(bucket)
    valid = True

    while collected < 1.00:
        spent = int(input(f"Insert money... \n"))
        if valid:
            time.sleep(0.3)
            match int(spent):
                case 1:
                    collected = collected + 1.00
                    print(f"{collected:.2f}")
                case 5:
                    collected = collected + 0.05
                    print(f"{collected:.2f}")
                case 10:
                    collected = collected + 0.10
                    print(f"{collected:.2f}")
                case 25:
                    collected = collected + 0.25
                    print(f"{collected:.2f}")
                case _:
                    print("Please insert $1 or correct change")

    vending_items()
    selection_option(collected)


collect_money()




