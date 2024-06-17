def main():
    x, y = get_fraction("Fraction: ")
    percent = fraction_to_percent(x,y)

    if 1 < percent < 99:
        print(f"{percent}%")

    elif percent >= 99:
        print("F")

    else :
        print("E")

def fraction_to_percent(x,y):
    return round((x/y)*100)

def get_fraction(promp):

        while True:
            fraction = input(promp)
            try:
                x = int(fraction.split("/")[0])
                y = int(fraction.split("/")[1])

            except (ValueError, ZeroDivisionError) :
                fraction = input(promp)

            else:
                if x>y:
                    continue
                else:
                    return x, y

if __name__ == "__main__":
    main()
