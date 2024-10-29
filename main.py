import yfinance as yf
import datetime


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = yf.Ticker(symbol)

    def price(self, date):
        end_date = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=10)
        historical_price = self.data.history(start=date, end=end_date.strftime('%Y-%m-%d'))
        if historical_price.empty:
            raise ValueError(f"No data available for {self.symbol} on {date}")
        return historical_price['Close'].iloc[0]


class Portfolio:
    def __init__(self, stocks):
        self.stocks = [Stock(stock) for stock in stocks]

    def profit_from_stock(self, index, start_date, end_date):
        try:
            start_price = float(self.stocks[index].price(start_date))
            end_price = float(self.stocks[index].price(end_date))
            return (end_price - start_price) / start_price
        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def profit(self, dates):
        start_date = dates[0]
        end_date = dates[1]
        profits_per_stock = {stock.symbol: self.profit_from_stock(i, start_date, end_date) for i, stock in enumerate(self.stocks)}
        total_profit = sum(profits_per_stock.values()) / len(self.stocks)
        return {
            'profits_per_stock': profits_per_stock,
            'total_profit': total_profit
        }


def validate_date(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def get_user_input():
    print("Welcome to Portfolio Profit Calculator!")
    print("\nEnter stock symbols separated by commas (e.g., AAPL,GOOG,MSFT):")
    symbols = input().strip().replace(' ', '').split(',')
    while True:
        print("\nEnter start date (YYYY-MM-DD):")
        start_date = input().strip()
        if validate_date(start_date):
            break
    
    while True:
        print("\nEnter end date (YYYY-MM-DD):")
        end_date = input().strip()
        if validate_date(end_date):
            break

    return symbols, [start_date, end_date]


if __name__ == "__main__":
    symbols, dates = get_user_input()
    portfolio = Portfolio(symbols)
    profits = portfolio.profit(dates)

    print("\nResults:")
    print("Profits per stock:")
    for symbol, profit in profits['profits_per_stock'].items():
        print(f"{symbol}: {profit*100:.2f}%")
    print(f"\nTotal portfolio profit: {profits['total_profit']*100:.2f}%")
