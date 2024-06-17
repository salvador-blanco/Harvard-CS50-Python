#Main function
def main():
    textpromp = input()
    textpromp_lw = indoor(textpromp)
    print(textpromp_lw)

#A function prompts the user and returns the lowercase
def indoor(textpromp):
    return textpromp.lower()

#Run main
main()
