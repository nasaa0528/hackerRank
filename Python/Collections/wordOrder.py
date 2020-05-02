# https://www.hackerrank.com/challenges/word-order/problem
from collections import OrderedDict
if __name__=='__main__':
	word_rep = OrderedDict() 
	for _ in range(int(input())): 
		word = input().strip()
		word_rep.setdefault(word,0)
		word_rep[word] += 1
		vals = [v for v in word_rep.values()]
	print(len(vals))
	print(*vals, sep=' ')
