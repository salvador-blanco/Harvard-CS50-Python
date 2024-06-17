def main():
    amount_due = 50
    change = ask_money(amount_due)
    print(f"Change Owed: {change}")

def ask_money(amount_due):
    while(amount_due > 0):
        print(f"Amount Due: {amount_due}")
        coin = input("Insert Coin: ")
        if coin == "25" or coin == "10" or coin == "5":
            amount_due -= int(coin)
    return -amount_due

if __name__ == "__main__":
    main()
