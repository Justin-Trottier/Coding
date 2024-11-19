import requests
import json
from datetime import datetime

# Get prices
def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

# Save prices to a file
def log_price(crypto_id, price):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('crypto_prices.log', 'a') as file:
        file.write(f"{timestamp} - {crypto_id}: ${price}\n")

# Main function
def main():
    print("Real-Time Cryptocurrency Tracker")
    crypto_ids = input("Enter the cryptocurrency IDs you want to track (comma-separated, e.g., bitcoin,ethereum): ")
    crypto_ids = [crypto.strip() for crypto in crypto_ids.split(',')]

    print("\nFetching prices...\n")
    for crypto_id in crypto_ids:
        try:
            price = get_crypto_price(crypto_id)
            print(f"The current price of {crypto_id} is: ${price:.2f}")
            log_price(crypto_id, price)
        except KeyError:
            print(f"Error: {crypto_id} is not a valid cryptocurrency ID or the API response is invalid.")

if __name__ == "__main__":
    main()