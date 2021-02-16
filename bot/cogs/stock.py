import discord
import sqlite3
import requests
from discord import Colour
from discord.ext import tasks, commands

async def get_ticker(ticker):
    pass

class StockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['stonk', 'stock'])
    async def stock(self, ctx):
        embed = discord.Embed().add_field().add_field()
        await ctx.send(embed=embed)

    # TODO:
    # example: !buy 5 BTC-USD
    @command.command()
    async def buy(self, ctx, shares: int, ticker: str):
        return True

    # TODO:
    @command.command()
    async def sell(self,):
        pass

    # TODO:
    @command.command()
    async def get_portfolio():
        pass

    # TODO:
    # Looks up and updates the stocks on the list of portfolios
    @tasks.loop(seconds=45)
    async def lookup():
        pass


def setup(bot):
    bot.add_cog(EmbedHelpCog(bot))

class MarketPlace(object):
    """docstring forMarketPlace."""

    def __init__(self):
        self.conn = sqlite3.connect('market.sqlite', check_same_thread=False) # to prevent multiple threads from accessing at same time
        self.cur = self.conn.cursor()
        self.requestQueue = {} # (ticker, last update-time, )
        # Database structure:
        # 2 tables:
        # stock table: (key: id-{text}, asset {commodity, crypto, stock}, ticker , buying price)
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
