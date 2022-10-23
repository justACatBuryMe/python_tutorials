a = input()
j = 0
d4 = 0
dn4 = 0
for i in range(len(a)):
    if a[i] == " ":
        if int(a[j:i])%4 == 0:
            d4 += 1
        else:
            dn4 += 1
        j = i+1
if int(a[j:])%4 == 0:
    d4 += 1
else:
    dn4 += 1
print(d4, dn4)
