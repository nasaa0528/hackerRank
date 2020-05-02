# https://www.hackerrank.com/challenges/any-or-all/problem
if __name__=='__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print((all([0 if i < 0 else i for i in arr])) and (any(True if i == i[::-1] else False for i in list(map(str,arr)))))
