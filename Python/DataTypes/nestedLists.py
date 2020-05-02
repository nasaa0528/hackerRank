#!/usr/bin/python3
# https://www.hackerrank.com/challenges/nested-list/problem
# Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':
    nestedList = [[input().strip(),float(input())] for _ in range(int(input()))]
    grades = [nestedList[i][1] for i in range(len(nestedList))]
    grades = list(set(grades))
    grades.sort()
    second_lowest = grades[1]
    names = [nestedList[i][0] for i in range(len(nestedList)) if nestedList[i][1] == second_lowest]
    names.sort()
    for n in names:
        print(n)
