#Task 1:


def calculate_average_closing_price(stock_data, stock_symbol, start_date, end_date):
    total_closing_price = 0
    count = 0
    for data_point in stock_data:
        symbol, date, closing_price = data_point
        if symbol == stock_symbol and start_date <= date <= end_date:
            total_closing_price += closing_price
            count += 1
    if count == 0:
        return None  # No data 
    else:
        return total_closing_price / count

# Sample stock data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

# Test function
average_price_aapl = calculate_average_closing_price(stock_data, "AAPL", "2021-01-01", "2021-01-02")
print("Average closing price of AAPL from 2021-01-01 to 2021-01-02:", average_price_aapl)

average_price_msft = calculate_average_closing_price(stock_data, "MSFT", "2021-01-01", "2021-01-01")
print("Average closing price of MSFT on 2021-01-01:", average_price_msft)
