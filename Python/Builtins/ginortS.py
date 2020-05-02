# https://www.hackerrank.com/challenges/ginorts/problem
s = list(input())
print("".join(sorted(s, key=lambda x:(not x.islower(), not x.isupper(), (x[-1] in ['0','2','4','6','8']), x))))
