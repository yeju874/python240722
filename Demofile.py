#Demofile.py

#파일 쓰기(유니코드)
f = open("demo.txt","wt",encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인")
f.close()

#파일 읽기
f = open("demo.txt","rt",encoding="utf-8")
result = f.read()
print(result)

#리스트로 받기
f.seek(0) #0바이트를 가리키도록 책갈피 역할
lst = f.readlines()
print(lst)

f.close()
