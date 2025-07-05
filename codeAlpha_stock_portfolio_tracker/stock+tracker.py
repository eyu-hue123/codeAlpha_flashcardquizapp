# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 135
}

portfolio = {}
total_value = 0

print(" Stock Portfolio Tracker")
print("Available Stocks: ", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print(" Invalid stock symbol. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print(" Please enter a valid number.")

# Calculate total value
print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n Total Investment Value: ${total_value}")

# Optional: Save to file
save = input("Do you want to save this to 'portfolio.txt'? (y/n): ").lower()
if save == 'y':
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${value}\n")
        f.write(f"\nTotal Investment Value: ${total_value}")
    print(" Portfolio saved to 'portfolio.txt'")