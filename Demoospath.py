# DemoOSpath.py

from os.path import *
from os import *

filename = "c:\\python310\\python.exe"

if exists(filename):
    print("파일 있음 : {0}".format(getsize(filename)))
else:
    print("파일 없음")

print(abspath("python.exe"))
print(basename(filename))

print("운영체제이름 : {0}".format(name))
#system("notepad.exe")

# 파일 목록 가져오기
import glob
print(glob.glob(r"c:\work\*.py"))