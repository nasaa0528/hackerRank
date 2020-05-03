# https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-regex
import re 
import email.utils
emailPattern = re.compile(r'^[a-zA-Z][a-zA-Z\d\._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
for _ in range(int(input())): 
    name, emailaddr = list(input().split())
    if emailaddr[0] == '<':
        emailaddr = emailaddr[1:]
    if emailaddr[-1] == '>':
        emailaddr = emailaddr[:-1]
    if emailPattern.search(emailaddr): 
        print(email.utils.formataddr((name,emailaddr)))
