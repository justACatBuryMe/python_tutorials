t12 = input()
t, p = t12.split()
if t12 == "12:00:00 midnight":
    print("08:00:00 midnight")
elif t12 == "08:00:00 A.M":
    print("08:00:00 midmorning")
elif t12 == "04:00:00 P.M":
    print("08:00:00 midevening")
elif p == "A.M":
    if int(t.split(":")[0]) < 8:
        print(t12)
    else:
        print("0", int(t.split(":")[0]) - 8, ":", ":".join(t.split(":")[1:]), " B.M", sep="")
else:
    if int(t.split(":")[0]) < 4:
        print("0", int(t12.split(":")[0]) + 4, ":", ":".join(t.split(":")[1:]), " B.M", sep="")
    else:
        print("0", int(t.split(":")[0]) - 4, ":", ":".join(t.split(":")[1:]), " C.M", sep="")
