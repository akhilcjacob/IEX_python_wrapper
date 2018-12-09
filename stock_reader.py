
import urllib.request, json
import json

# This class simplifies the access to IEX

class StockReader():
    def __init__(self):
        self.base_url = "https://api.iextrading.com/1.0"
    

    # Returns the json formatted data of a url
    def grab_data(self, url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data

    # Returns the most active stocks of the day
    def get_most_active(self):
        url = self.base_url + '/tops/last/'
        return self.grab_data(url)

    # Returns the information of a stock over a time period
    # symbol:  official stock symbol { ie. aapl }
    # timeFrame: period of time to get data for 
    #           dynamic: returns 1d or 1m based on time of data
    #           date: yyyymmdd
    #           1m, 3m, 6m, 1y, 2y, 5y
    #           ytd: year to date    
    def get_stock(self, symbol, timeFrame='1y'):
        url = self.base_url+'/stock/'+symbol+'/quote/' +timeFrame
        return self.grab_data(url)
    
    # Returns information about the company
    # symbol:  official stock symbol { ie. aapl }
    def get_company_information(self, symbol):
        url = self.base_url + '/stock/'+symbol
        return self.grab_data(url)
    
    # Returns information about crypto market
    def get_crypto(self):
        url = self.base_url
        return self.grab_data(url)
    
    # Returns infromation about the divdends
    # symbol:  official stock symbol { ie. aapl }
    # timeFrame: period of time to get data for 
    #           dynamic: returns 1d or 1m based on time of data
    #           date: yyyymmdd
    #           1m, 3m, 6m, 1y, 2y, 5y
    #           ytd: year to date    
    def get_dividends(self, symbol, timeFrame='1y'):
        url = self.base_url+'/stock/'+symbol+'/dividents/' +timeFrame
        return self.grab_data(url)
    
    # Returns earning report from 4 most recent quarters
    # symbol:  official stock symbol { ie. aapl }
    def get_earnings(self, symbol):
        url = self.base_url+'/stock/'+symbol+'/earnings/'
        return self.grab_data(url)
    
    # 
    # symbol:  official stock symbol { ie. aapl }
    def get_market_earnings(self):
        url = self.base_url+'/stock/market/today-earnings/'
        return self.grab_data(url)
    
    # symbol:  official stock symbol { ie. aapl }
    def get_effective_spread(self, symbol):
        url = self.base_url+'/stock/'+symbol+'/effective-spread/'
        return self.grab_data(url)

    # symbol:  official stock symbol { ie. aapl }
    def get_financials(self, symbol):
        url = self.base_url+'/stock/'+symbol+'/financials/'
        return self.grab_data(url)

