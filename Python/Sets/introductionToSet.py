#!/usr/bin/python3
"""
Example tests: 
print(set('HackerRank')) # characters will have different orders
print(set([1,2,1,2,3,4,5,6,0,9,12,22,3]))
print(set((1,2,3,4,5,5)))
print(set(set(['H','a','c','k','e','r','r','a','n','k'])))
print(set({'Hacker' : 'DOSHI', 'Rank' : 616 }))
print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))
"""
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Task: 
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
# Formula Avg = (SumOfDistinctHeights) / (TotalNumberOfDistinctHeights)
def average(array):
	return sum(set(array))/len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # arr = [161,182,161,154,176,170,167,171,170,174]
    result = average(arr)
    print(result)