taco_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    total_bill = 0
    prompt = "Item: "

    while True:

        item_price = get_item_price(prompt, taco_menu)
        if item_price == "exit":
            break

        total_bill += item_price
        total_bill = round(total_bill,2)
        print("Total: ${:.2f}".format(total_bill ))


def get_item_price(prompt, menu):
    while True:
        try:
            item = input(prompt)
        except EOFError:
            return "exit"

        try:
            item_price = menu[item.title()]
        except KeyError:
            pass
        else:
            return item_price

if __name__ == "__main__":
    main()

