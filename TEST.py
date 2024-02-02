a = [1,2,3,4,[6,7,8]] #리스트 자료
b = [6,7,8]
print(a)
print(a[-1][2]) #리스트 인덱싱
print(a[4][:-1])   #리스트 슬라이스
print(a*3) #리스트 연산자
print(len(a[4]))
a[2] = 7
print(a)
print(b in a)
print(a.append(6))
print(a.count(6))
print(a)

import sys

print(sys.path)