from utils import FinanceData
import cx_Oracle


def main():
    apple = FinanceData(ticker="AAPL")
    apple.get_stock_info()
    apple_data = apple.get_data(10)
    connection = cx_Oracle.connect(user="system", password="oracle",
                                   dsn="localhost:1521")


if __name__ == '__main__':
    main()
