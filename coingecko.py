import requests

def get_market_data(category):
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Sort by percentage change in the specified time
        gainers = sorted(data, key=lambda x: x[f"price_change_percentage_{category}_in_currency"] or 0, reverse=True)[:10]
        losers = sorted(data, key=lambda x: x[f"price_change_percentage_{category}_in_currency"] or 0)[:10]

        return gainers, losers
    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], []

def display_results(timeframe, gainers, losers):
    print(f"\nTop 10 {timeframe} Gainers:")
    for coin in gainers:
        print(f"{coin['name']} ({coin['symbol'].upper()}): {coin[f'price_change_percentage_{timeframe}_in_currency']:.2f}%")

    print(f"\nTop 10 {timeframe} Losers:")
    for coin in losers:
        print(f"{coin['name']} ({coin['symbol'].upper()}): {coin[f'price_change_percentage_{timeframe}_in_currency']:.2f}%")

def main():
    timeframes = {
        "1h": "1h",
        "24h": "24h",
        "7d": "7d",
        "30d": "30d"
    }

    for key, category in timeframes.items():
        gainers, losers = get_market_data(category)
        display_results(key, gainers, losers)

if __name__ == "__main__":
    main()
