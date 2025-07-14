n = int(input())
if n<=0 or n>=20:
    print("Invalid")
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            if (i==1 or i==n or j==1 or j==i):
                print("1",end=" ")
            else:
                print("0",end=" ")
        print()