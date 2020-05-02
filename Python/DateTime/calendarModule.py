import calendar as cd
if __name__=='__main__':
    mm,dd,yy = list(map(int, input().split()))
    print(cd.day_name[cd.weekday(yy,mm,dd)].upper())
