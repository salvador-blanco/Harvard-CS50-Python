def main():

    promp = "Date: "

    while True:
        outdated_date = get_date(promp)
        date =  me_to_iso(outdated_date)
        if date == "error":
            pass
        else:
            print(date)
            break


def get_date(promp):
        return input(promp).strip()

def me_numeric_to_iso(outdated_date):

    m, d, y = outdated_date.split("/")

    m = int(m)
    d = int(d)
    y = int(y)

    return y, m, d

def me_text_to_iso(outdated_date):
    months_lst = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    m, d, y = outdated_date.split(" ")
    d = int(d[:-1]) #Remove comma
    m = int(months_lst.index(m)+1)
    y = int(y)

    return y, m, d

def me_to_iso(outdated_date):
    if outdated_date[0].isdecimal():
        try:
            y, m, d = me_numeric_to_iso(outdated_date) # middle-endian
        except ValueError:
            return "error"
    else:
        try:
            y, m, d = me_text_to_iso(outdated_date)
        except ValueError:
            return "error"

    if m > 12 or d>31:
         return "error"
    else:
        return "{:04}-{:02}-{:02}".format(y,m,d)



if __name__ == "__main__":
    main()
