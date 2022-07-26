import tweepy.errors

from tweet import Twitter
from scrape_website import Stock
from datetime import datetime


now = datetime.now().strftime("%Y-%m-%d %H:%M UTC-8")
twitter = Twitter()
stock = Stock()

# TODO append status updates to database, MongoDB?

status = stock.check_stock()
if status:
    # TODO create bool for status flip so account doesn't repeatedly tweet the item is in stock, only notifies when
    #  it changes status
    try:
        twitter.tweet(f'N64 switch controller is no longer out of stock. Check it now: https://bit.ly/3z6rc6H\n\n'
                      f'\nLast Checked: {now}')
    except tweepy.errors.Forbidden:
        # TODO create log
        print("ERROR! DUPLICATE TWEET!")
else:
    # TODO change below to something more elegant
    print("ITEM IS STILL OUT OF STOCK.")