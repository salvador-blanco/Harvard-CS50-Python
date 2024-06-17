def main():
    tweet = input("Input: ")
    twt = tweet_to_twt(tweet)
    print(f"Output: {twt}")

def tweet_to_twt(tweet):
    twt = ""
    for i in tweet:
        if i.lower() in "aeiou":
            continue
        else:
            twt += i
    return twt
if __name__ == "__main__":
    main()
