s = "12:12:12PM"
p = s[8]
h, m, s = [int(i) for i in s[:8].split(":")]
if p == "P":
    h += 12
else:
    if h == 12:
        h = 0
print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")

