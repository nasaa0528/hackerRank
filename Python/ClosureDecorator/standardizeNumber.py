# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
def wrapper(f):
    def fun(l):
        prefix = '+91 '
        for i in range(len(l)): 
            if (len(l[i]) == 10): 
                l[i] = prefix + l[i][:5] + " " + l[i][5:]
            elif (len(l[i]) == 11 and l[i][0] == '0'):
                l[i] = prefix + l[i][1:6] + " " + l[i][6:]
            elif (len(l[i]) == 12 and l[i][0:2] == '91'): 
                l[i] = prefix + l[i][2:7] + " " + l[i][7:]
            elif (len(l[i]) == 13 and l[i][0:3] == '+91'): 
                l[i] = prefix + l[i][3:8] + " " + l[i][8:]
        return f(l)
    return fun

# sort_phone = wrapper(sort_phone)
# sort_phone = sortnum( l changed, then called)  
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



