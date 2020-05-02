#!/usr/bin/python3
# https://www.hackerrank.com/challenges/py-set-union/problem
# a.union(b) = a | b, when a and b are sets 
# s = set("Hacher")
# print(s)
# print(s.union("Rank"))
# print(s.union(enumerate(['R', 'a', 'n', 'k'])))
# for k,v in enumerate(['R', 'a', 'n', 'k']): 
#     print(k, v)

# Task: 
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
if __name__=='__main__': 
    n = int(input())
    eng_set = set(map(int, input().split()))
    b = int(input())
    fr_set = set(map(int,input().split()))
    total_sub = eng_set.union(fr_set)
    print(len(total_sub))
