#!/usr/bin/python3
from math import log

# Q1
print("--- Q1")
a = 4
b = 2
c = a+b
print(c)

# Q2
print("--- Q2")
sum = 0
n = 5
for i in range(n):
    sum += int(input("|->> "))
avg = sum/n
print(avg)

# Q3
print("--- Q3")
n = int(input("|->>"))
if n%2 == 0:
    print("even")
else:
    print("odd")

# Q4
print("--- Q4")
p = int(input("|->> "))
r = int(input("|->> "))
t = int(input("|->> "))
si = p*r*t/100
print(si)

# Q5
print("--- Q5")
grades = float(input("|->> "))
if grades > 100:
    print("Error")
elif grades > 90:
    print("S")
elif grades > 80:
    print("A")
elif grades > 70:
    print("B")
elif grades > 60:
    print("C")
elif grades > 50:
    print("D")
elif grades >= 0:
    print("F")
else:
    print("Error")

# Q6
print("--- Q6")
age = float(input("|->>"))
if age < 0 or age > 100:
    exit()
print("yes" if age >= 18 else "no")

# Q7
print("--- Q7")
enrollment_number = int(input("|->>"))
print(enrollment_number % 10)

# Q8
print("--- Q8")
name = input("|->>")
print(name[-1], name[0])

# Q9
print("--- Q9")
income = float(input("|->>"))
if income <= 5:
    print("No Tax")
elif income <= 10:
    print(f"{income/10}")
elif income <= 25:
    print(f"{income*20/3}")
else:
    print(f"{income/4}")

# Q10
print("--- Q10")
n = int(input("|->>"))
for i in range(1,11):   print(n+i)

# Q11
print("--- Q11")
for i in range(1,6):
    print(int(5*(10**i - 1)/9))

# Q12
print("--- Q12")
n = int(input("|->>"))
print(10*n + 55)

# Q13
print("--- Q13")
n = int(input("|->>"))
for i in range(1,11):   print(n*i)

# Q14
print("--- Q14")
n = int(input("|->>"))
m = 0
digits = round(log(n)/log(10))
for i in range(digits+1):
    print((n%10) * (10**(digits-i)))
    m += (n%10) * (10**(digits-i))
    n //= 10
print(m)

# Q15
print("--- Q15")
n = int(input("|->>"))
print(round(log(n)/log(10))+1)
