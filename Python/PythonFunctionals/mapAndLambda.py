# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
cube = lambda x: x**3

def fibonacci(n):
    fibs = []
    for i in range(n):
        if (i == 0):
            fibs.append(0)
        elif (i == 1):
            fibs.append(1)
        else:
            fibs.append(fibs[-1]+fibs[-2])
    return fibs

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
