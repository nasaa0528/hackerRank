#!/bin/python3
from datetime import datetime
from datetime import timedelta

def time_delta(t1, t2):
    t1 = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    difference = (t1-t2)
    return (str(abs(int(difference.total_seconds()))))
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
