#A while loop
i = 1
while i < 10:
    print(i)
    i += 1

#With break statement
j = 1
while j < 7:
    print(j)
    if j == 4:
        break
    j += 1

#With continue statement
f = 0
while f < 7:
    f += 1
    if f == 3:
        continue
    print(f)

#With else statement
d = 1
while d < 8:
    print(d)
    d += 1
else:
    print("d is no longer less than 8")