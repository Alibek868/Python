tupel1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3, 34, 231)
tuple3 = (True, False, False)

print(tupel1)
print(tuple2)
print(tuple3)

#What is the data type of the tupels
mytuple = ("apple", "kiwi", "cucumber")
print(type(mytuple))
print('\n')

#update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = 'kiwi'
x = tuple(y)

print(x)


#Add item for tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
print('\n')
#add tuple for tuple 
thesetuple = ("Mercedes", "Toyota", "Cherry")
y = ("KIA",)
thesetuple += y
print(thesetuple)
print('\n')

#loop through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    print('\n')

# range() and len() functions to create suitable iterable
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
