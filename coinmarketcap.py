import requests
from prettytable import PrettyTable
api = 'https://api.coinmarketcap.com/v2/ticker/'

raw_data = requests.get(api).json()
data = raw_data['data']

table = PrettyTable()

for currency in data:
    name = data[currency]['name']
    price = data[currency]['quotes']['USD']['price']
    change_1h = data[currency]['quotes']['USD']['percent_change_1h']
    change_24h = data[currency]['quotes']['USD']['percent_change_24h']
    change_7d = data[currency]['quotes']['USD']['percent_change_7d']


    if float(change_24h) > 0:
     table.add_row([name, price, change_1h, change_24h, change_24h])
     table.fiels_names = ["Name", "Price", "Change 1h", "Change 24h", "Change 7d"]
     table.sortby = "Change 24h"
     table.reversesort = True


    print(table)

print(data)

