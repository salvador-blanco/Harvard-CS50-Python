def main():
    time = convert(input("What time is it? ").lower().strip())
    eating_time = eating_time_calc(time)
    print(eating_time)


def convert(time):
    hour, minutes = map(float, time.split(":"))
    return hour + minutes/60

def eating_time_calc(time):

    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"
    else:
        return ""

if __name__ == "__main__":
    main()
