#Function.py

#함수정의
def setValue(newValue):
    #지역변수
    x=newValue
    print("지역변수:", x)

#호출
retValue = setValue(5)
print(retValue)

#기본값명시
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자 : 매개변수명 호출

def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

#호출
print(connectURI("multi.com","80"))
print(connectURI(port="8080", server="multi.com"))

#이름해석
x = 5
def func(a):
   return a+x
print(func(1))

def func2(a):
    x = 2
    return a+x

#호출
print(func2(1))

#가변인자
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#람다함수
g = lambda x,y : x*y
print( g(2,3)) 
print((lambda x:x*x)(3))
print (globals())


#for 함수

score = int(input("점수를 입력:"))

if 90<= score <= 100:
    grade = "A"
elif 80<= score <90:
    grade = "B"
elif 70<= score < 80:
    grade = "C"
else :
    grade = "D" 

print ("grade is:" + grade)




