# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 120,
    "MSFT": 310
}

a_port = {}

print("Enter your stock portfolio:")
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in the price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue
    a_port[stock] = a_port.get(stock, 0) + quantity

total_value = 0
print("\nYour Portfolio:")
for stock, quantity in a_port.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock} - Qty: {quantity}, Price: ${price}, Value: ${value}")

print(f"\nTotal Investment Value: ${total_value}")

save = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, 'w') as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, quantity in a.items():
            price = stock_prices[stock]
            value = price * quantity
            f.write(f"{stock},{quantity},{price},{value}\n")
        f.write(f"\nTotal Investment Value,,,{total_value}\n")
    print(f"Portfolio saved to {filename}")
