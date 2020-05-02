#!/usr/bin/python3
# https://www.hackerrank.com/challenges/python-lists/problem
# Consider a list (list = []). You can perform the following commands:

# 1.insert i e:     Insert integer e at position i.
# 2.print:          Print the list.
# 3.remove e:       Delete the first occurrence of integer e.
# 4.append e:       Insert integer 3 at the end of the list.
# 5.sort:           Sort the list.
# 6.pop:            Pop the last element from the list.
# 7.reverse:        Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list
if __name__ == '__main__':
    n = int(input())
    l = [] 
    for _ in range(n): 
        command = input().strip().lower().split()
        if len(command) == 1: 
            cmd = command.pop() 
            if cmd == 'print': 
                print(l)
            elif cmd == 'sort':
                l.sort() 
            elif cmd == 'reverse':
                l.reverse()
            elif cmd == 'pop': 
                l.pop()
            else: 
                print("unknown command") 
        elif len(command) == 2: 
            cmd = command.pop(0)
            val = int(command.pop())
            if cmd == 'append': 
                l.append(val)
            elif cmd == 'remove': 
                l.remove(val)
            else: 
                print("Unknown command") 
        elif len(command) == 3: 
            cmd = command.pop(0) 
            val = int(command.pop())
            ind = int(command.pop())
            if cmd == "insert": 
                l.insert(ind,val)
            else: 
                print("unknown command") 
        else: 
            print("unknown command")

