#!/usr/bin/python3
# https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
	num_ti = int(len(string) / k)
	for i in range(num_ti): 
		ti = string[i*k:(i+1)*k]
		ti = list(ti)
		ui = []
		for ch in ti: 
			if ch not in ui: 
				ui.append(ch)
		ui = "".join(ui)
		print(ui)

if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)