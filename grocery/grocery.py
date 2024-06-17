def main():
    grocery_list = []
    grocery_dict = {}
    promp = ""

    while True:
        new_item = get_item(promp)
        if new_item == "exit":
            break

        grocery_list.append(new_item)

    grocery_list.sort()
    grocery_dict = count_list(grocery_list)
    print_grocery_dictionary(grocery_dict)

def print_grocery_dictionary(grocery_dict):
    print()
    for i in grocery_dict:
        print(f"{grocery_dict[i]} {i}")

def count_list(grocery_list):
    grocery_dict = {}
    for i in grocery_list:
        try:
            grocery_dict[i] += 1
        except KeyError:
            grocery_dict[i] = 1
    return grocery_dict



def get_item(promp):
    try:
        item = input(promp).upper()
        return item
    except EOFError:
        return "exit"

if __name__ == "__main__":
    main()
