""" Design a Python script to determine the difference in date for given two dates in YYYY:MM:DD format (0 <= YYYY <= 9999, 1 <= MM <= 12, 1 <= DD <= 31) following the leap year rules. """
a=input("Enter first date:")
b=a.split("/")
c=input("Enter second date:")
d=c.split("/")
diff=0
for i in range(3):
    res=int(b[i])-int(d[i])
    if i==0:
        res=res*1
    elif i==1:
        res=res*30
    elif i==2:
        res=res*365
    diff=diff+res
if diff<0:
    print(-(diff),"Days")
else:
    print(diff,"Days")
print(diff*24,"Hours")
print(diff*24*60,"mintues")
print(diff*24*60*60,"seconds")
