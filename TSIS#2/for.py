fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# with the break statement we can stop the loop before it has looped through all the items
cars = ["Mercedes", "Toyota", "BMW", "Porshe", "Wolsvagen"]
for x in cars:
    
    if x == "Toyota":
        break
    print(x)

#with continue
cars = ["Mercedes", "Toyota", "BMW", "Porshe", "Wolsvagen"]
for x in cars:
    if x == "Toyota":
        continue
    print(x)

#The range() function
for x in range(2, 30, 6):
    print(x)

#print 
for x in range(6):
  print(x)
else:
  print("Finally finished!") 

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

#For with pass statements
for x in [0, 1, 2]:
  pass

