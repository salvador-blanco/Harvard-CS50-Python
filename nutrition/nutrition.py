def main():
    item = input("Item: ").lower()
    calories = get_calories(item)
    if calories != "":
        print(f"Calories: {calories}")
    else:
        print(calories)
        
def get_calories(item):
    calories_dictionary = {
        'apple': 130,
        'avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew melon': 50,
        'kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80
        }

    if item in calories_dictionary.keys():

        return calories_dictionary[item]
    else:
        return ""

if __name__ == "__main__":
    main()
