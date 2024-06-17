def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (2 <= len(s) <= 6):
        if(s[0].isalpha() and s[1].isalpha()):
            if check_decimal(s):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def check_decimal(s):
    for i in range(len(s)-1,1,-1):
        if s[i-1].isdecimal() == True and s[i].isdecimal() == False:
            return False

        elif s[i-1].isdecimal() == False and s[i].isdecimal() == True:
            if s[i] == "0":
                return False
    else:
        return True



if __name__ == "__main__":
    main()
