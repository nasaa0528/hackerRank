#!/usr/bin/python3
# https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    # approach 1 
    #string = list(string) 
    #string[position] = character 
    #string = "".join(string)
    string = string[:position] + character + string[position+1:]
    return string 

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
