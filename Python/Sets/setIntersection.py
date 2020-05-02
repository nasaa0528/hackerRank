#!/usr/bin/python3
# .intersection() - returns intersection of set and set of elements in an iterable 
# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.
if __name__=='__main__': 
	n = int(input())
	eng_set = set(map(int,input().split()))
	b = int(input())
	fr_set = set(map(int, input().split()))
	both = eng_set.intersection(fr_set)
	print(len(both))