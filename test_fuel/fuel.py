def main():
    percentage = get_fraction("Fraction: ")
    print(gauge(percentage))

def get_fraction(promp):

        while True:
            fraction_str = input(promp)
            try:
               fraction = convert(fraction_str)
            except (ValueError, ZeroDivisionError) :
                pass
            else:
                return fraction

def convert(fraction):

    x = int(fraction.split("/")[0])
    y = int(fraction.split("/")[1])

    if x>y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError

    return fraction_to_percent(x,y)

def fraction_to_percent(x,y):
    return round((x/y)*100)

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"

    elif percentage >= 99:
        return "F"

    else :
        return "E"

if __name__ == "__main__":
    main()
