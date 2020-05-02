# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
items = OrderedDict()
for _ in range(int(input())): 
    line = list(input().split())
    net_price = int(line[-1]) 
    item_name = " ".join(line[:-1])
    items.setdefault(item_name,0)
    items[item_name] += net_price
for k,v in items.items(): 
    print(k,v)
