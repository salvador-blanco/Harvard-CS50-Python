import sys
import csv
from tabulate import tabulate

def main():
    filename = get_filename(sys.argv)
    table_list = read_csv(filename)
    print(tabulate(table_list[1:] , table_list[0], tablefmt = 'grid'))

def get_filename(argv):
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(argv) < 2:
        sys.exit("Too few command-line arguments")

    file_name = argv[1]
    if file_name.endswith(".csv"):
        return file_name
    else:
        sys.exit("Not a Python file")

def read_csv(filename):
    table = []
    with open(filename) as f:
        try:
            csv_file = csv.reader(f)
        except IndexError:
            exit("Error reading the file")
        for line in csv_file:
            table.append(line)
    return table

if __name__ == "__main__":
    main()
