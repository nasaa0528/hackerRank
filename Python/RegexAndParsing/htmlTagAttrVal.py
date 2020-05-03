# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        if attrs: 
            for attr in attrs: 
                print('-> {} > {}'.format(attr[0], attr[1]))    
    def handle_startendtag(self,tag,attrs):
        print(tag)
        if attrs: 
            for attr in attrs: 
                print('-> {} > {}'.format(attr[0], attr[1]))

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
