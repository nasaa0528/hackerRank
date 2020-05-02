# https://www.hackerrank.com/challenges/input/problem
if __name__=='__main__':
    x,k = map(int, input().split())
    if k == eval(input()):
        print(True)
    else:
        print(False)

