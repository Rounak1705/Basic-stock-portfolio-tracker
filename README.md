# Basic-stock-portfolio-tracker
Build a simple stock tracker that calculates total investment based on manually defined stock prices.


📈 Stock Portfolio CSV Manager (Python)

A simple and efficient Python project that calculates stock portfolio value and exports the data into a CSV file.

This project is useful for beginners who want to learn:

- Python dictionaries
- File handling
- CSV operations
- Basic finance-related calculations

---

🚀 Features

- Stores stock prices using Python dictionaries
- Maintains stock quantity in a portfolio
- Calculates total value for each stock
- Computes total investment value
- Exports all data to a CSV file
- Handles missing stock price cases

---

🛠️ Technologies Used

- Python 3
- CSV Module (Built-in Python Library)

---

📂 Project Structure

stock-portfolio/

├── main.py
├── Portfolio.csv
|── README.md

---

💻 Code Overview

The program performs the following steps:

1. Defines stock prices
2. Defines stock quantities in portfolio
3. Calculates individual stock value
4. Calculates total investment
5. Saves the data into "Portfolio.csv"

---

📌 Example Code

import csv

Stock_price = {
    "AAPL": 180,
    "TSLA": 250
}

portfolio = {
    "AAPL": 28,
    "TSLA": 15
}

---

📊 Sample Output (CSV)

Stock,Price,Quantity,Total
AAPL,180,28,5040
TSLA,250,15,3750

Total Investment,,,8790

---

▶️ How to Run

Run the following command in terminal:

python main.py

After execution, a file named Portfolio.csv will be created.

---

📈 Output Message

Data saved to Portfolio.csv

---

🎯 Learning Concepts Covered

- Dictionaries in Python
- "for" loop
- Conditional statements
- CSV writing using "csv.writer()"
- File handling with "with open()"

---

🔮 Future Improvements

You can upgrade this project by adding:

- User input for stocks
- Real-time stock prices using APIs
- Profit/Loss calculator
- Graph visualization
- Portfolio diversification analysis

---

👨‍💻 Author

Developed by Rounak Pan

---
