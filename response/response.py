import validators

def main():
    if not validators.email(input("What's your email address? ")):
        print("Invalid")
    else:
        print("Valid")


if __name__ == "__main__":
    main()
