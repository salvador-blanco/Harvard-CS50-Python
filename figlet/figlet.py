import pyfiglet
import sys

def main():
    if len(sys.argv) == 3:
        font = select_font(sys.argv[1:])
    elif len(sys.argv) == 1:
        font = "slant"
    else:
        sys.exit("No arguments")

    text = input("Input: ")
    print(f"Output: {pyfiglet.figlet_format(text, font = font)}")

def select_font(arguments):
        if arguments[0] == "-f" or aarguments[0] == "--f":
            return arguments[1]
        else:
            sys.exit("Check arguments")

if __name__ == "__main__":
    main()
