#If statements
a = 33
b = 200
if b > a:
    print("b is greater than a")

#the elif keyboard is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# The else keyboard cathches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#Short hand if ... else statements
a = 2
b = 303
print("a") if a > b else print("B")

#multiple statement on the same line
a = 330
b = 330
print("a") if a > b else print("=") if a == b else print("B") 

# Nested If 
x = 41

if x > 10:
    print("Above ten, ")
    if x > 20:
        print("and also above twenty! ")
    else:
        print("But not above twenty! ")