def main():
    camel = input("camelCase: ")
    snake = camel_to_snake(camel)
    print(f"snake_case: {snake}")

def camel_to_snake(camel):
    snake = ""

    for i in camel:
        if i.isupper():
            snake += "_" + str.lower(i)
        else:
            snake += i
    return snake

if __name__ == "__main__":
    main()
