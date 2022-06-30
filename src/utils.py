import yfinance as yf


class FinanceData:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.stock = yf.Ticker(self.ticker)

    def get_data(self, days: int):
        data = self.stock.history(period=f"{days}d")
        print(data.head())
        return data

    def get_stock_info(self):
        print(self.stock.info)
        return self.stock.info
