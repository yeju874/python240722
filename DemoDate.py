#DemoDate.py

from datetime import *

#print(dir())
 
d1 = date(2024, 7, 23)
print(d1)
print(date.today())
print(datetime.now())

#문자열가공
nowDate = date(2024,7,10).strftime("%Y/%m/%d")
print(nowDate)

import random

print(random.random())
print( [random.randrange(20) for i in range(10)] )
print( random.sample(range(30), 5)) #unique 한 수 추출
