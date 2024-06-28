import re


list =input()
find = re.findall("ab*", list)
print(find)
if find:
    print("YES")
else:
    print("NO")    