#!/usr/bin/python3 
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    # s = input()
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)