
import urllib.request, json
import json
from inspect import signature
# This class simplifies the access to IEX

class StockReader():
    def __init__(self):
        self.base_url = "https://api.iextrading.com/1.0"
    
    ## ========================================================= ##
    ## Functions that combine lower level functions to generate useful
    ## ========================================================= ##
    def get_market_rundown(self):
        rundown = {}
        rundown["earnings"] = self.get_market_earnings()
        rundown["crypto"] = self.get_crypto()
        rundown["sector_perfomance"] = self.get_sector_performance()
        rundown["upcoming_ipos"] = self.get_upcoming_ipos()
        rundown["most_active"] = self.get_most_active()
        return rundown
        
    def get_snapshot (self, symbol):
        qSnapshot_details=["logo",'price','stats']
        snapshot = {}
        for detail in qSnapshot_details:
            snapshot['detail'] = self.get_stock_detail(symbol, detail)
    ## ========================================================= ##
    # Functions that return information about a specific company
    ## ========================================================= ##

    # Runs a get function for multiple symbols and returns a dictionary; format:{"StockSymbol": [...obtained json obj...]}
    # functionToRun: choose a function to run must be function that pulls data for a single company
    #           {ie get_stock, get_company_information} doesn't support get_most_active, get_crypto etc.
    # symbol: run function against a list of stocks
    # timeFrame (optional): choose time bucket (default: 1y)
    def run_against_multiple(self, functionToRun, symbols, timeFrame='1y', detail=None):
        output = {}
        for symbol in symbols:
            # Get signature of a function to check for what args it requries
            sig = signature(functionToRun)
            if len(sig.parameters) == 1:
                raise ValueError("The selected function doesn't handle symbols")
            if len(sig.parameters) == 2:
                output[symbol] = functionToRun(symbol)
            if len(sig.parameters) == 3 and detail == None:
                output[symbol] = functionToRun(symbol, timeFrame)
            if len(sig.parameters) == 3 and detail != None:
                output[symbol] = functionToRun(symbol, detail)

    # Returns the information of a stock over a time period as a json object
    # symbol:  official stock symbol { ie. aapl }
    # timeFrame: period of time to get data for 
    #           dynamic: returns 1d or 1m based on time of data
    #           date: yyyymmdd
    #           1m, 3m, 6m, 1y, 2y, 5y
    #           ytd: year to date/stock/market/crypto    
    def get_stock(self, symbol, timeFrame='1y'):
        url = self.base_url+'/stock/'+symbol+'/quote/' +timeFrame
        return self.grab_data(url)
    
    # Returns a specfic detail about a particular stock
    # symbol:  official stock symbol { ie. aapl }
    # detail: choose the detail to get
    #       largest-trades: 
    #       company: information about a company
    #       earnings: Data from the four most recent quarters
    #       effective-spread: 
    #       financials: income statement, balance sheet, cash flow
    #       threshold-securities:
    #       short-interest: 
    #       stats: key stats about the company
    #       logo: returns image url
    #       ohlc: returns open/close prices
    #       peers: returns stocks similar to current symbol
    #       previous: returns stock information about the previous day
    #       price: from the last 15 minutes
    #       quote: snapshot of information
    #       relevant: fallback for peers detail
    #       company: information about the company
    #       delayed-quote: return/stock/market/cryptos 15 min delayed market quote
    #       earnings: pulls data frm reported quarters 
    #       financials: 
    def get_stock_detail(self, symbol, detail):
        url = self.base_url + '/stock/'+symbol+'/'+detail+'/'
        return self.grab_data(url)
   

    
    # Returns infromation about the divdends as a json object
    # symbol:  official stock symbol { ie. aapl }
    # timeFrame: period of time to get data for 
    #           dynamic: returns 1d or 1m based on time of data
    #           date: yyyymmdd
    #           1m, 3m, 6m, 1y, 2y, 5y
    #           ytd: year to date    
    def get_dividends(self, symbol, timeFrame='1y'):
        url = self.base_url+'/stock/'+symbol+'/dividends/' +timeFrame
        return self.grab_data(url)
    

    # Returns news about the company
    # symbol:  official stock symbol { ie. aapl }
    # numberOfArticles: pull this many articles
    def get_news(self, symbol, numberOfArticles):
        url = self.base_url+'/stock/'+symbol+'/last/'+numberOfArticles
        return self.grab_data(url)

    # Returns the history of the stock price for a particular stock as a json obj
    # symbol:  official stock symbol { ie. aapl }
    # timeFrame: period of time to get data for 
    #           dynamic: returns 1d or 1m based on time of data
    #           date: yyyymmdd
    #           1m, 3m, 6m, 1y, 2y, 5y
    #           ytd: year to date    
    def get_chart(self, symbol, timeFrame='1y'):
        url = self.base_url+'/stock/'+symbol+'/chart/' +timeFrame
        return self.grab_data(url)

        
    ## ========================================================= ##
    # Functions that return information about the market status
    ## ========================================================= ##

    # Returns market earning for today as a json object
    # symbol:  official stock symbol { ie. aapl }
    def get_market_earnings(self):
        url = self.base_url+'/stock/market/today-earnings/'
        return self.grab_data(url)

    # Returns IPOS of the month as a json object
    def get_upcoming_ipos(self):
        url = self.base_url+'/stock/market/upcoming-ipos'
        return self.grab_data(url)

    # Returns Todays IPOS as a json object
    def get_todays_ipos(self):
        url = self.base_url+'/stock/market/today-ipos'
        return self.grab_data(url)

    # Returns todays market performance as a json object
    def get_sector_performance(self):
        url = self.base_url+'/stock/market/sector-performance'
        return self.grab_data(url)

        # Returns information about crypto market as a json object
    def get_crypto(self):
        url = self.base_url +'/stock/market/crypto'
        return self.grab_data(url)
    
    # Returns the most active stocks of the day
    def get_most_active(self):
        url = self.base_url + '/tops/last/'
        return self.grab_data(url)

    # Returns all symbols
    def get_symbols (self):
        url = self.base_url + '/ref-data/symbols'
        return self.grab_data(url)    

    # Returns the json formatted data of a url
    def grab_data(self, url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data
    

x  = StockReader()
x.get_market_rundown()