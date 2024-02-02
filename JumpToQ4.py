## 1. 주어진 자연수가 홀수인지, 짝수인지 판별해 주는 함수 is_odd를 작성해보자. 홀수이면 True, 짝수이면 False

def is_odd(number) :
    if(number%2==1) :
        return True
    else :
        return False

## 2. 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. 단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.

def avg_numbers(**args) :
    result = 0
    for i in args :
        result += i
    return result/len(args)

## 3. 2개의 숫자를 입력받아 더한 후에 리턴하는 프로그램이다.
## 3과 6을 입력했을 때 9가 아닌 36 이라는 결괏값이 출력되었다.  이 프로그램의 오류를 수정해 보자.

input1 = input("첫 번째 숫자를 입력하세요 :")
input2 = input("두 번째 숫자를 입력하세요 :")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다" % total)

## 4. 다음 중 출력 결과가 다른 하나를 골라보자

print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join["you","need","python"])

## 3번 ',' 쉽표는 띄어쓰기가 됨.

## 5. 다음은 파일(test.txt)에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

## 6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
user_input = input("저장할 내용을 입력하세요 :")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()

## 7. 다음과 같은 내용을 지닌 test.txt가 있다. 이 파일의 내용중 "java" 라는 문자열을 "python"으로 바꾸어 저장해 보자.
###  Life is too short
###  you need java

f = open('test.txt', 'r')
body = f.read()
f.close()
body = body.replace("java", "python")
f = open('test.txt', 'w')
f.write(body)
f.close()

## 8. 입력값을 모두 더해 출력하는 스크립트 (C:\doit\myargv.py)를 작성해 보자.
### C:\> cd doit
### c:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10

import sys

args = sys.argv[1:]
result = 0
for i in args :
    result += int(i)
print(result)
