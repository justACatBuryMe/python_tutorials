l=int(input())
u=int(input())
# if u in range(0,1001) and l in range(0,1001) and l<u:
x=0
if u%3==0 and u%5!=0:
    print("You entered fizz")
elif u%5==0 and u%3!=0:
    print("You entered buzz")
elif u%3==0 and u%5==0:
    print("You entered fizzbizz")
else:
    print("You entered ordinary")
for j in range(u-1,l-1):
    if j%3==0:
        print(" fizz")
# for j in range(x,l-1,-1):
    if j%3==0 and j%5!=0:
        print("fizz")
    elif j%5==0 and j%3!=0:
        print("buzz")
    elif j%3==0 and j%5==0:
        print("fizzbizz")
    else:
        print(j)
    break
