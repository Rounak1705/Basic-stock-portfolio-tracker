import csv

# Define Stock & Price
Stock_price={
    "AAPL" : 180,
    "TSLA" : 250
}

# Define portfolio (Stock + Quantity)
portifolio={
    "AAPL" : 28,
    "TSLA" : 15
}

total_value=0

with open("Portfolio.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Stock","Price", "Quantity", "Total"])
    for stock,qty in portifolio.items():
        if stock in Stock_price:

            price=Stock_price[stock]
            value=price*qty
            total_value+=value
            writer.writerow([stock, price, qty, value])
        else:
            print(f"Price not available for {stock}")
    writer.writerow([])
    writer.writerow(["Total Invesment","","",total_value])
print("Data saved to portfolio.csv")