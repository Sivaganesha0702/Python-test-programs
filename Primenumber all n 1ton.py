count=0
n=int(input("Enter a Number: "))
print("List of prime number between 1 to ",n)
for i in range(1,n+1):
    cn=i #current number
    count=0
    for j in range(1,cn+1):
        if cn%j == 0:
            count +=1
    if count == 2: #2 if prime
        print(cn)