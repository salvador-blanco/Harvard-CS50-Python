import emoji

def main():
   emojiless_string = input("Input: ")
   emoji_string = emoji.emojize(emojiless_string, language='alias')
   print(f"Output: {emoji_string}")

if __name__ == "__main__":
    main()
