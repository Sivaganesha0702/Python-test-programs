n=int(input("Enter a Number: "))
t=n
r=0
while(n>0):
    a=n%10
    r=r+a*a*a
    n=n//10
if(r==t):
    print(t,"is a Armstrong Number")
else:
    print(t,"is not a Armstrong Number")