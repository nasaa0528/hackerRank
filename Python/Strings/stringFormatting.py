#!/usr/bin/python3
# https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    width = len(format(number,'b'))
    for i in range(1,number+1):
        print(
                str(i).rjust(width), 
                format(i,'o').rjust(width),
                format(i, 'X').rjust(width), 
                format(i, 'b').rjust(width)
            )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)