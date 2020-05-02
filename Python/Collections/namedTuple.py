# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
from collections import namedtuple 
if __name__=='__main__': 
	students = []
	num_students = int(input())
	c = list(input().split())
	Student = namedtuple('Student', c)
	for _ in range(num_students): 
	    row = input().split()
	    for i in range(len(row)): 
	        if c[i] != "NAME": 
	            row[i] = int(row[i])
	    x1,x2,x3,x4 = row
	    students.append(Student(x1,x2,x3,x4))
	grades = sum([s.MARKS for s in students])/num_students
	print("{:.2f}".format(grades))
