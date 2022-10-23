n = int(input( ))
# m = -n//2+2
# while m < n//2+1:
#     if m < 0:
#         o = -m
#     else:
#         o = m
#     print("*"*n)
#     print(" "*o+"*")
#     m += 2
# print("*"*n)
# for i in range(n):
#     if(0==(i%2)):
#         print("*"*n)
#         continue
#     if(i<=n//2):
#         print(" "*((n//2)-i)+"*")
#     if(i>n//2):
#         print(" "*(i-(n//2))+"*")
for i in range(-n//2+2, n//2, 2):
    o = -i if i < 0 else i
    print("*"*n)
    print(" "*o+"*")
print("*"*n)

