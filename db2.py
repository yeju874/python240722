#db2.py
import sqlite3

#연결객체 (파일에저장)
con = sqlite3.connect(r"c:\work\sample.db")

#커서객체 (생성과 같은거 사용하기위해)
cur = con.cursor()

#테이블 구조 생성
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

#1건입력
cur.execute("insert into PhoneBook values ('yeju', '010-2639');")

#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);",(name, phoneNumber))

#여러건 입력
datalist = (("변유진", "010-333"), ("유현정", "010-444"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#검색결과
cur.execute("select * from PhoneBook;")
print("---fetch one---")
print(cur.fetchone())
print("---fetch two---")
print(cur.fetchmany(2))
print("---fetch all---")
print(cur.fetchall())
cur.execute("select * from PhoneBook;")
con.commit()

# for row in cur:
#     print(row)
