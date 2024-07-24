#web1.py

from bs4 import BeautifulSoup

#페이지 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#검색이 용이한 스프객체
soup = BeautifulSoup(page, "html.parser") # 두번째 태그는 정해져있는것. html태그 가지고있으면 html.parser
# print(soup.prettify()) #전체문서 그대로 출력
# <p> 전체 검색
# print(soup.find_all("p"))
#첫번째 <p>태그만 가져오기
# print(soup.find("p"))
#조건 지정해서 검색하기 : <p class ='outer-text'>
# print(soup.find_all("p" , class_="outer-text")) # class 라는 매개변수와 겹치므로 밑에 언더바 하나 넣음 class_
#print(soup.find_all("p" , attrs={"class":"outer-text"}))
#id=first
#print(soup.find_all(id="first"))

#내부 문자열 출력
for tag in soup.find_all("p"):
    title = tag.text.strip() #앞뒤 공백 없애고 가져와
    title = title.replace("\n","")
    print(title)