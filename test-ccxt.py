import ccxt
import time

symbol = 'BTCUSDT'
buy_price_threshold = 60000
sell_price_threshold = 68000
trade_quantity = 0.001


# Binance Testnet configuration
client = ccxt.binance({
    'apiKey': 'wWmQTlUgKTN5ijmke0baRsqJJdXkJYNT4MuuLIzh1W3btohk2b1EYKXHVGNLOUj7',
    'secret': 'gzgKQEVjKFvth4P2kdsxBNS7iwfX5j8l123R6R4CI5731wLjz4IVOgm8fWO0NuUw',
    'enableRateLimit': True,
})

# Switch to the Testnet endpoint
client.set_sandbox_mode(True)

def get_current_price(symbol):
    ticker = client.fetch_ticker(symbol)
    return float(ticker['last'])

def get_balance():
    return client.fetch_balance()

def place_buy_order(symbol, quantity):
    order = client.create_market_buy_order(symbol=symbol, amount=quantity)
    print(f"Buy order done: {order}")

def place_sell_order(symbol, quantity):
    order = client.create_market_sell_order(symbol=symbol, amount=quantity)
    print(f"Sell order done: {order}")

def trading_bot():
    in_position = False

    while True:
        current_price = get_current_price(symbol)
        print(f"Current price of {symbol}: {current_price}")

        if not in_position:
            if current_price < buy_price_threshold:
                print(f"Price is below {buy_price_threshold} -> Place BUY order!")
                place_buy_order(symbol, trade_quantity)
                in_position = True
            else:
                if current_price > sell_price_threshold:
                    print(f"Price is above {sell_price_threshold} -> Place SELL order!")
                    place_buy_order(symbol, trade_quantity)
                    in_position = False

            time.sleep(2)

if __name__ == "__main__":
    trading_bot()


