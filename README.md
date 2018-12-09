Single File Python wrapper around the IEX API


# About:

The python file 'stock_reader.py' pulls in data from the [IEX 
API](https://iextrading.com/developer/docs/#getting-started).

## Basic Usage:
	
	reader = StockReader()
	print(reader.get_most_active())
	print(reader.get_stock('aapl',timeFrame ='5y'))

## Available Functions:

NAME
    stock_reader

CLASSES
        StockReader
    
    class StockReader(builtins.object)
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  get_company_information(self, symbol)
     |      # Returns information about the company
     |      # symbol:  official stock symbol { ie. aapl }
     |  
     |  get_crypto(self)
     |      # Returns information about crypto market
     |  
     |  get_dividends(self, symbol, timeFrame='1y')
     |      # Returns infromation about the divdends
     |      # symbol:  official stock symbol { ie. aapl }
     |      # timeFrame: period of time to get data for 
     |      #           dynamic: returns 1d or 1m based on time of data
     |      #           date: yyyymmdd
     |      #           1m, 3m, 6m, 1y, 2y, 5y
     |      #           ytd: year to date
     |  
     |  get_earnings(self, symbol)
     |      # Returns earning report from 4 most recent quarters
     |      # symbol:  official stock symbol { ie. aapl }
     |  
     |  get_effective_spread(self, symbol)
     |      # symbol:  official stock symbol { ie. aapl }
     |  
     |  get_financials(self, symbol)
     |      # symbol:  official stock symbol { ie. aapl }
     |  
     |  get_market_earnings(self)
     |      # symbol:  official stock symbol { ie. aapl }
     |  
     |  get_most_active(self)
     |      # Returns the most active stocks of the day
     |  
     |  get_stock(self, symbol, timeFrame='1y')
     |      # Returns the information of a stock over a time period
     |      # symbol:  official stock symbol { ie. aapl }
     |      # timeFrame: period of time to get data for 
     |      #           dynamic: returns 1d or 1m based on time of data
     |      #           date: yyyymmdd
     |      #           1m, 3m, 6m, 1y, 2y, 5y
     |      #           ytd: year to date
     |  
     |  grab_data(self, url)
     |      # Returns the json formatted data of a url


