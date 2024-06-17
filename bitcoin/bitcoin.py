import sys
import json
import requests

def main():

    bitcoin_n = bitcoin_from_argv()
    bitcoin_price = get_bitcoin_price()
    bitcoin_amount = bitcoin_n * bitcoin_price
    print( f"${bitcoin_amount:,.4f}" )

def get_bitcoin_price():
    BITCOIN_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        b_j = json.loads(requests.get(BITCOIN_URL).text)
    except requests.RequestException:
        exit("URL not reachable")

    bitcoin = float( b_j["bpi"]["USD"]["rate_float"])

    return(bitcoin)

def bitcoin_from_argv():
    try:
        bitcoin = float(sys.argv[1])
        return bitcoin
    except ValueError:
        exit("Missing command-line argument")
    except IndexError:
        exit("Missing command-line argument")

if __name__ == "__main__":
    main()
