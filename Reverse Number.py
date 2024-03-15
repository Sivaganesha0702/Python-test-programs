n=int(input("Enter a number to reverse: "))
rev=0
while(n!=0):
    rev=rev*10
    rev=rev + n % 10
    n=n//10
print("Reverse number of entered number is ",rev)