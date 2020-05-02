# https://www.hackerrank.com/challenges/zipped/problem
if __name__=='__main__':
    n,x = map(int, input().split())
    grades = []
    for _ in range(x):
        grades.append(list(map(float, input().split())))
    [print(sum(grds)/len(grds)) for grds in (list(zip(*grades)))]


