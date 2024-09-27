from binance.client import Client
import time

API_KEY = 'wWmQTlUgKTN5ijmke0baRsqJJdXkJYNT4MuuLIzh1W3btohk2b1EYKXHVGNLOUj7'
API_SECRET = 'gzgKQEVjKFvth4P2kdsxBNS7iwfX5j8l123R6R4CI5731wLjz4IVOgm8fWO0NuUw'

client = Client(API_KEY, API_SECRET, testnet=True)
#acc = client.get_account()

symbol = 'BTCUSDT'
buy_price_threshold = 60000
sell_price_threshold = 68000
trade_quantity = 0.001

def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

get_current_price(symbol)

def place_buy_order(symbol, quantity):
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    print(f"Buy order done: {order}")

def place_sell_order(symbol, quantity):
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
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



