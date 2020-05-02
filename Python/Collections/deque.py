# https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
if __name__=='__main__':
    d = deque()
    for _ in range(int(input())): 
        cmd = input().split()
        if (cmd[0] == 'append'): 
            d.append(int(cmd[-1]))
        elif (cmd[0] == 'pop'):
            d.pop() 
        elif (cmd[0] == 'popleft'): 
            d.popleft()
        elif (cmd[0] == 'appendleft'): 
            d.appendleft(int(cmd[-1]))
    print(*d, sep=' ')
