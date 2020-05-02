# https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque
def pop(l): 
    if (l[0] > l[-1]):
        popped = l.popleft()
    elif (l[0] <= l[-1]):
        popped = l.pop()
    return popped 

if __name__=='__main__':
    for _ in range(int(input())): 
        res = "Yes"
        n = int(input())
        horizontal_pile = deque(list(map(int,input().split())))
        popped = 0
        while(horizontal_pile): 
            if (popped == 0):
                popped = pop(horizontal_pile)
            else: 
                next_pop = pop(horizontal_pile)
                if (popped < next_pop):
                    res = "No"
                    break
        print(res)

