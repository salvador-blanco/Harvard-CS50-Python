import sys

def main():

    file_name = get_filename(sys.argv)
    lines = read_file(file_name)
    n_lines = count_lines(lines)
    print(n_lines)

def count_lines(lines):
    n_lines = 0
    for line in lines:
        line = line.strip()

        if line == "":
            continue
        elif line[0] == "#":
            continue
        else:
            n_lines += 1
    return n_lines


def read_file(file_name):
    lines = []
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    return lines

def get_filename(argv):
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(argv) < 2:
        sys.exit("Too few command-line arguments")

    file_name = argv[1]
    if file_name.endswith(".py"):
        return file_name
    else:
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
