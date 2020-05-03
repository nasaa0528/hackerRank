# https://www.hackerrank.com/challenges/html-parser-part-2/problem
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data): 
        data = data.split('\n')
        data = list(filter(lambda x: len(x) > 0, data))
        if data: 
            print(">>> Data")
            print(*data)
    def handle_comment(self, data):
        data = data.split('\n')
        if (len(data) == 1):
            print(">>> Single-line Comment")
            print(*data)
        else: 
            print(">>> Multi-line Comment")
            print(*data, sep='\n')
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
