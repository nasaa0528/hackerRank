#!/usr/bin/python3
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
def print_rangoli(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = alphabet[:n]
    width = (n-1)*4 + 1
    for i in range(1,2*n):
        if i < n: 
            num = i 
        elif (i == n): 
            num = n
        elif (i > n): 
            num = (2 * n) % i
        # print(i, num)
        line = letters[-num:]
        if len(line) != 1: 
            line = (line[::-1] + line[1:])
        line = '-'.join(list(line))
        print(line.center(width, '-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)