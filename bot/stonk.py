import sqlite3
import io
import json
import urllib3

http = urllib3.PoolManager()

'''
# Purpose: Helper function for getting stocks data,
# Args: stock ticker
# Returns: json data for stock from yahoo finance api
# Ex: getStonk('AMD') => {price: 15, currency: USD, ... }
'''
def getStonk(stonk):
    r = http.request('GET', "https://query1.finance.yahoo.com/v7/finance/quote?symbols=" + stonk)
    return json.loads(r.data)

'''
# Purpose: Helper functoin to determine if historic
# Args: json data
# Returns: True if historic, false if not
# Ex: checkHistoric(getStonk("AMD")) => false
'''
def checkHistoric(data):
    historic = False
    prunedData = {"name": "", "tradable": True, curr_price = ""}
    return {historic, prunedData}

'''
# Stock trader object
# Has: Money, stocks, id
# How to init: can load from database (give id, stocks, and money)
# Can: Trade money for stocks
       Liquidate stocks
       Give money to another trader
       Get money from another trader
'''
class Trader(object):
    """docstring for Trader."""

    def __init__(self, arg):
        super(Trader, self).__init__()
        self.arg = arg

    '''
    Function that can override what stocks and how much money a trader has
    ONLY USE IF THERE IS AN OUTAGE
    '''
    def giftFromGod(stonks, monies):
        return False

    '''
    Function that attempts to sell stock
    '''
    def sellStonk():
        return False

    '''
    Function that attempts to buy stock
    '''
    def buyStonk():
        return False

    '''
    Function that takes away some money that you have, percentage based
    '''
    def taxation(percent):
        return False

    '''
    Same as taxation, just a set amount of money however
    '''
    def taxation_Ammount(amount):
        return False

    '''
    Function that adds money to your account
    '''
    def gift(amount):
        return False

print(getStonk("AMD"))
