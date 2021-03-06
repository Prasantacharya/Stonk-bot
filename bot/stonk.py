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

class MarketPlace(object):
    """docstring forMarketPlace."""

    def __init__(self):
        self.conn = sqlite3.connect('market.sqlite', check_same_thread=False) # to prevent multiple threads from accessing at same time
        self.cur = self.conn.cursor()
        self.requestQueue = {} # (ticker, last update-time, )
        # Database structure:
        # 2 tables:
        # stock table: (key: id-{text}, asset {commodity, crypto, stock})
        # person table: (key: id-{text}, money-{double precision})
        self.cur.execute("""CREATE TABLE IF NOT EXISTS stockAccount(
                    id       INT
                    , asset  varchar(10)
                    , amount FLOAT
                    );""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS bankAccount(
                    id       INT
                    , amount DOUBLE
                    );""")

    # default adding a person to the account
    def add_account(self, id):
        self.cur.executescript("""IF NOT EXISTS (SELECT * FROM stockAccount WHERE id = ?)
        INSERT INTO stockaccount VALUES(?,NULL,0);
        """, (id,))
        self.cur.execute("INSERT INTO bankaccount VALUES(?, ?);", (id, 5000))
        self.conn.commit()
        return True

    def remove_account(self, id):
        return True

    def buy_stock(self, userID, ticker, shares, pricePerShare):
        if (pricePerShare * shares) > (self.cur.execute("SELECT")):
            return False
        return True

    def sell_stock(self, userID, ticker, shares, money):
        return True

    def add_money(self, userID, money):
        return True

    def tax_money(self, userID, money):
        return True

    def tax_percent(self, percent):
        # Affects all users
        return True

    def getAccount(self, id):
        self.cur.execute("SELECT * FROM stockAccount WHERE id = ?;", id):
        return self.cur.fetchone();

    # Money gets
    def tax_return(self, money):
        # Affects all users
        return True

    def get_stock():
        return True
