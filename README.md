# Portfolio Profit Calculator

A Python tool to calculate stock portfolio profits using historical market data from Yahoo Finance.

## Features
- Calculate profits for multiple stocks between two dates
- Calculate annualized returns for better performance comparison
- User-friendly command line interface
- Percentage-based profit calculations per stock and total portfolio

## Calculations
The tool provides two key metrics:
- Regular profit: ((end_price - start_price) / start_price)
- Annualized return: (1 + total_profit)^(365/days_between_dates) - 1

The annualized return normalizes the profit over a year period, making it easier to compare investments held for different lengths of time.

## Requirements
- Python 3.9+

## Setup
1. Create a virtual environment:
```bash
python -m venv myenv

# On MacOS and Linux:
source myenv/bin/activate
# On Windows:
myenv\Scripts\activate
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```
## Usage
1. Run the script:
```bash
python main.py
```
2. Follow the prompts to enter the stock symbols, start date, and end date.
3. The script will calculate the percentage-based profit for each stock and the total portfolio.
## Example
```
Welcome to Portfolio Profit Calculator!

Enter stock symbols separated by commas (e.g., AAPL,GOOG,MSFT):
AAPL,GOOG

Enter start date (YYYY-MM-DD):
2023-01-01

Enter end date (YYYY-MM-DD):
2023-12-31

Results:
Profits per stock:
AAPL: 48.25%
GOOG: 52.37%

Total portfolio profit: 50.31%
```