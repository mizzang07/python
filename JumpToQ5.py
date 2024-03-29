## 1. 다음은 Calculator 클래스이다.
## 이 클래스를 상속하는 UpgradCalculator를 만들고 갑을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.

class Calculator:
    def __init__(self) :
        self.value = 0

    def add(self, val) :
        self.value += val

class UpgradCalculator(Calculator) :
    def minus(self, val) :
        self.value -= val

cal = UpgradCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

## 2. 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.

class MaxLimitCalculator(Calculator) :
    def add(self, val) : 
        self.value += val
        if self.value > 100 :
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

## 3. 다음 결과를 예측해보자
'''''
all([1, 2, abs(-3)-3])  -- > 거짓

chr(ord('a')) == a  --> 참... 
'''
## 4. filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3] 에서 음수를 모두 제거해보자

result = list(filter(lambda x : x >0 , [1, -2, 3, -5, 8, -3]))
print(result)


## 5. 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
## hex(234)
## '0xea'
## 이번에는 반대로 16진수 문자열 '0xea'를 10진수로 변경해보자

print(int('0xea', 16))



## 6. map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요곳값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어보자

print(list(map(lambda x : x*3, [1, 2, 3, 4])))


## 7. 다음 리스트의 최댓값과 최솟값의 합을 구해보자

a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a) + min(a))



## 8. 17/3 의 결과는 5.666666666667 이다. 결괏값을 소숫점 4자리까지만 반올림하여 표시해보자.

print(round(17/3, 4))


## 9. os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해보자.
### 1. C:\doit 디렉터리로 이동한다.
### 2. dir 명령을 실행하고 그 결과를 변수에 담는다.
### 3. dir 명령의 결과를 출력한다.

import os
os.chdir("D:\만화")
os.system("dir")
a= os.popen("dir")
print(a.read())


## 10. glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해보자.


import glob
print(glob.glob("D:\만화\*.py"))


## 11. time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자
### 2018/04/03 17:20:32

import time
a=  time.strftime("%Y/%m/%d %X") 
print(a)


## 12. random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단, 중복된 숫자가 있으면 안 됨).

import random

print(random.sample(range(1, 46), 6))



## 13. 영철이 누나의 생일은 1995년 11월 20일이고 영철이의 생일은 1998년 10월 6일이다. 영철이 누나는 영철이보다 며칠 더 먼저 태어났을까?

import datetime

day1 = datetime.date(1995, 11, 20)
day2 = datetime.date(1998, 10, 6)
diff = day2 - day1
print(diff.days)



## 14. 기록순으로 data를 정렬해보자
import operator

data = [('윤서현', 15.25),
        ('김예지', 13.31),
        ('박예원', 15.34),
        ('송순자', 15.57),
        ('김시우', 15.48),
        ('배숙자', 17.9),
        ('전정웅', 13.39),
        ('김혜진', 16.63),
        ('최보람', 17.14),
        ('한지영', 14.83),
        ('이성호', 17.7)
]

print(sorted(data, key=operator.itemgetter(1), reverse=True))


## 15. 다음 4명의 학생 중 청소 당번 2명을 뽑을 수 있는 경우의 수를 모두 나열하시오.
import itertools

data = ['나지혜', '성성민', '윤지현', '김정숙']

print(list(itertools.combinations(data, 2)))



## 16. "abcd" 문자열을 나영하는 경우의 수를 다음과 같이 모두 출력하시오
### abcd, abdc, adcd, (...생략...)

data = "abcd"

for a, b, c, d in itertools.permutations(data, 4) :
    print(a+b+c+d , end=", ")


## 17. ['김승현', '김진호', '강춘자', '이예준', '김현주'] 다음 5명이 있다.
##     ['청소', '빨래', '설거지'] 해야할 일은 3가지가 있다.
##5명을 무작위로 섞어 앞의 3명에게 차례로 해야 할 일인 ["청소", "빨래", "설거지"]를 지정하고 나머지 2명에게는 "휴식"을 지정할 수 있는 프로그램을 작성하시오

import itertools
a = random.sample(['김승현', '김진호', '강춘자', '이예준', '김현주'], 5)
b = ['청소', '빨래', '설거지']

print(list(itertools.zip_longest(a, b, fillvalue = "휴식")))


## 18. 가로의 길이는 200cm이고 세로의 길이는 80cm인 벽이 있다. 이 벽에 되도록 큰 정사각형 모양의 타일을 붙이려고 한다.
## 이때 붙이려는 타일 한 선의 길이와 붙이는 데 필요한 타일의 개수를 구하시오.

import math

gcd = math.gcd(200, 80)

print(gcd) 
print((200*80)/(gcd*gcd))
