#!/usr/bin/python3 
# .remove(x) - removes x from set, if x doesn't exist, then raise key error
# .discard(x) - removes x from set, but doesn't raise error when x doesn't appear in set. 
# .pop() - Removes and returns arbitrary element from set. If no element to remove, then raises KeyError
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# task 
# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
if __name__=='__main__': 
	n = int(input())
	s = set(map(int, input().split()))
	for _ in range(int(input())): 
		command = input().split()
		if len(command) == 1 and command[0].lower() == 'pop': 
			s.pop()
		elif len(command) == 2 and command[0].lower() == 'remove': 
			s.remove(int(command[1]))
		elif len(command) == 2 and command[0].lower() == 'discard': 
			s.discard(int(command[1]))
		else: 
			print("Error")
	print(sum(s))