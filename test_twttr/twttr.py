def main():
    word = input("Input: ")
    twt = shorten(word)
    print(f"Output: {twt}")

def shorten(word):
    twt = ""
    for i in word:
        if i.lower() in "aeiou":#if i in "aeiou":
            continue
        else:
            twt += i
    return twt

if __name__ == "__main__":
    main()
