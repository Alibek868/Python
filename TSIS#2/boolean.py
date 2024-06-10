print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#in this case all are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#folllowing will return true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))