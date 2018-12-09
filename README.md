Single File Python wrapper around the IEX API


# About:

The python file 'stock_reader.py' pulls in data from the [IEX 
API](https://iextrading.com/developer/docs/#getting-started).

## Basic Usage:
	
	reader = StockReader()
	print(reader.get_most_active())
	print(reader.get_stock('aapl',timeFrame ='5y'))

## Available Functions:

    
    class StockReader(builtins.object)
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  get_chart(self, symbol, timeFrame='1y')
     |      # Returns the history of the stock price for a particular stock as a json obj
     |      # symbol:  official stock symbol { ie. aapl }
     |      # timeFrame: period of time to get data for 
     |      #           dynamic: returns 1d or 1m based on time of data
     |      #           date: yyyymmdd
     |      #           1m, 3m, 6m, 1y, 2y, 5y
     |      #           ytd: year to date
     |  
     |  get_crypto(self)
     |  
     |  get_dividends(self, symbol, timeFrame='1y')
     |      # Returns infromation about the divdends as a json object
     |      # symbol:  official stock symbol { ie. aapl }
     |      # timeFrame: period of time to get data for 
     |      #           dynamic: returns 1d or 1m based on time of data
     |      #           date: yyyymmdd
     |      #           1m, 3m, 6m, 1y, 2y, 5y
     |      #           ytd: year to date
     |  
     |  get_market_earnings(self)
     |      # Returns market earning for today as a json object
     |      # symbol:  official stock symbol { ie. aapl }
     |  
     |  get_market_rundown(self)
     |  get_most_active(self)
     |      # Returns the most active stocks of the day
     |  
     |  get_news(self, symbol, numberOfArticles)
     |      # Returns news about the company
     |      # symbol:  official stock symbol { ie. aapl }
     |      # numberOfArticles: pull this many articles
     |  
     |  get_sector_performance(self)
     |      # Returns todays market performance as a json object
     |  
     |  get_snapshot(self, symbol)
     |  
     |  get_stock(self, symbol, timeFrame='1y')
     |      # Returns the information of a stock over a time period as a json object
     |      # symbol:  official stock symbol { ie. aapl }
     |      # timeFrame: period of time to get data for 
     |      #           dynamic: returns 1d or 1m based on time of data
     |      #           date: yyyymmdd
     |      #           1m, 3m, 6m, 1y, 2y, 5y
     |      #           ytd: year to date/stock/market/crypto
     |  
     |  get_stock_detail(self, symbol, detail)
     |      # Returns a specfic detail about a particular stock
     |      # symbol:  official stock symbol { ie. aapl }
     |      # detail: choose the detail to get
     |      #       largest-trades: 
     |      #       company: information about a company
     |      #       earnings: Data from the four most recent quarters
     |      #       effective-spread: 
     |      #       financials: income statement, balance sheet, cash flow
     |      #       threshold-securities:
     |      #       short-interest: 
     |      #       stats: key stats about the company
     |      #       logo: returns image url
     |      #       ohlc: returns open/close prices
     |      #       peers: returns stocks similar to current symbol
     |      #       previous: returns stock information about the previous day
     |      #       price: from the last 15 minutes
     |      #       quote: snapshot of information
     |      #       relevant: fallback for peers detail
     |      #       company: information about the company
     |      #       delayed-quote: return/stock/market/cryptos 15 min delayed market quote
     |      #       earnings: pulls data frm reported quarters 
     |      #       financials:
     |  
     |  get_symbols(self)
     |      # Returns all symbols
     |  
     |  get_todays_ipos(self)
     |      # Returns Todays IPOS as a json object
     |  
     |  get_upcoming_ipos(self)
     |      # Returns IPOS of the month as a json object
     |  
     |  grab_data(self, url)
     |      # Returns the json formatted data of a url
     |  
     |  run_against_multiple(self, functionToRun, symbols, timeFrame='1y', detail=None)
     |      # Runs a get function for multiple symbols and returns a dictionary; format:{"StockSymbol": [...obtained json obj...]}
     |      # functionToRun: choose a function to run must be function that pulls data for a single company
     |      #           {ie get_stock, get_company_information} doesn't support get_most_active, get_crypto etc.
     |      # symbol: run function against a list of stocks
     |      # timeFrame (optional): choose time bucket (default: 1y)
     |  
     |  