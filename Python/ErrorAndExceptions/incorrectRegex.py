import re 
if __name__=='__main__':
    for _ in range(int(input())):
        regex = input()
        try: 
            mo = re.compile(regex)
            print(True)
        except: 
            print(False) 
