# https://www.hackerrank.com/challenges/exceptions/problem
if __name__=='__main__': 
	for _ in range(int(input())): 
		m,n = input().split()
		try:
			print(int(m) // int(n))
		except ZeroDivisionError as e: 
			print("Error Code:", e)
		except ValueError as e: 
			print("Error Code:", e)
