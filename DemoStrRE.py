# DemoStrRe.py

data = "<<<   spam and ham   >>>"
result = data.strip("<> ")
print(data)
print(result)

strA = "python is very powerful"
upper = strA.upper()
print(upper)
print(len(strA))
print(len(upper))
print(strA.capitalize()) #앞글자만 대문자로 변경
print(upper.lower())
print(strA.replace("python","C#"))
lst = strA.split()
print(lst)
print(" ".join(lst))


#정규 표현식
import re

result = re.search("[0-9]*th","35th") #숫자가 0회이상 반복
print(result)
print(result.group()) # 찾은 단어만 보여줌

result = re.search("\d{4}", "올해는 2024년 입니다") #숫자가 연속으로 네자리 있는것
print(result.group())