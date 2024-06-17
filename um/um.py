import re

def main():
    print(count(input("Text: ")))

def count(s):
    um_list = re.findall(r"([^a-z]u+m+[^a-z?])", " "+s+" ", re.IGNORECASE)
    for u in um_list:
        print(u)
    return len(um_list)

if __name__ == "__main__":
    main()
