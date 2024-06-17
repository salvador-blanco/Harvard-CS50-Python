import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    youtube = re.search(r"^<iframe.+https?://(?:www\.)?youtube.com/embed/([a-z0-9]+)", s.strip(), re.IGNORECASE)
    if bool(youtube):
        return "https://youtu.be/" + youtube[1]
    else:
        return None

if __name__ == "__main__":
    main()
