#DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

lst = ["apple", 10, 10.5]
for item in lst:
    print(item)

# 리스트 함축 연습
lst = [1,2,3,4,5]
print([i**2 for i in lst if i<4])
t = ("apple","banana","orange")
print([len(i) for i in t])
d = {100:"apple",200:"banana",300:"orange"}
print([v.upper() for v in d.values()])