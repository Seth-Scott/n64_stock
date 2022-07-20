from tweet import Twitter
from scrape_website import Stock

twitter = Twitter()
stock = Stock()

status = stock.check_stock()
if status:
    # TODO create bool for status flip so account doesn't repeatedly tweet the item is in stock, only notifies when
    #  it changes status
    twitter.tweet('N64 switch controller is no longer out of stock. Check it now')

else:
    twitter.tweet("success")

# TODO exception handling for tweepy.errors.Forbidden (187 - Status is a duplicate)