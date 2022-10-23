n=int(input())
for i in range(n):
    print("*"*(n-i), "*"*(i)," "*(i-2),"*"*(n-i),end="")
    print()
for i in range(2,n+1):
    print("*"*(i)," "*(n-i)," "*(n-i),"*"*(i),end="")
    print()
