p = int(input())
for i in [len(l := [ i for i in range(1, int(p**0.5) + 1) if p%i == 0 ])]+l: print(i, int(p/i))
