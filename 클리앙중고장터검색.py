# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우 디코딩
        page = data.decode('utf-8', 'ignore') #글자 깨져도 무시
        #스프 객체
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

# <span class="subject_fixed" data-role="list-title-text" title="아이폰12프로 128블루 (택포 39만)">
# 아이폰12프로 128블루 (택포 39만)
# </span>
        for item in list:
                #에러처리 구문
                try:

                        title = item.text.strip()
                        #print(title)
                        if (re.search('아이폰', title)):
                                print(title.strip())
                except:
                        pass #혹시 에러가 나면 에외사항 패스
        
