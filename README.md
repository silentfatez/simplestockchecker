Simple Stock Checker
============


This is a simple pricing calculator to determine if a stock should be bought or not using the valuation calculator in this video https://youtu.be/nX2DcXOrtuo
 packages required
 ## Warnings
  Note: this is just a gauger of the markets and is not intended to be a one stop tool for you to buy shares

## Getting Started

### Prerequisites
You will need certain packages to use this tool
```sh
 pip install yahoo_fin
 pip install requests_html
 pip install pandas
 ```
 ## Usage
```sh
python simplestockpricer.py
 ```
 type in the ticker for the stock that you want. Currently only works for Nasdaq stocks.
 The minimum rate is 0.15 and the margin of safety is 0.33. You can tweak it in the file.
 
 The price to buy the stock at will be printed followed by the current price of the stock. 
 The reccomendation is then printed.
 
 ## Acknowledgements
 https://youtu.be/nX2DcXOrtuo
 http://theautomatic.net/yahoo_fin-documentation/#get_stats
