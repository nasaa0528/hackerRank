# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re 
repeatPattern = re.compile(r'.*([\d])\1{3}.*')
cardPattern = re.compile(r'^[456][\d]{3}\-?[\d]{4}\-?[\d]{4}\-?[\d]{4}\-?$')
for _ in range(int(input())): 
    cardNum = input() 
    if cardPattern.search(cardNum) and not repeatPattern.search("".join(cardNum.split("-"))):
        print("Valid")
    else: 
        print("Invalid")
