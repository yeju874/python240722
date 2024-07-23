#Demofilter.py

lst = [10,25,30]
iterL = filter(None,lst)
for item in iterL:
    print("Item:{0}".format(item))

def getBiggerThan20(i):
    return i>20
print("---필터링함수사용---")
iterL = filter(getBiggerThan20,lst)
for item in iterL:
    print("Item:{0}".format(item))

print("---람다함수사용---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print("Item:{0}".format(item))