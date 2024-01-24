import datetime as dt
a = dt.datetime(2024,1,20)
b = dt.datetime.now()
"""print(a.time)
print(b)"""

if a > b :
    print("오늘 이후")
elif a < b :
    print("오늘 이전")
else :
    print("오늘")
"""
c = [1,2,3,4,5]
for k in range(len(c)) :
    print(k)

c = [[1,2,3],[4,5,6],[7,8,9]]
for j in range(len(c)) :
    for k in range(len(c[j])) :
        print(c[j][k])

result = 0
i=1
while i <= 1000:
    if i %3==0 :
        result += i
    i += 1
print(result)


i="*"
cnt = 1
while cnt <= 5 :
    print(i*cnt)
    cnt += 1

i=0
while True :
    i += 1
    if i>5 :break
    print ('*'*i)


for i in range(1, 101)  :
    print( i )


A= [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for i in A :
    total += i
average = total/len(A)
print(average)

"""
# 리스트컴프리헨션
number = [1,2,3,4,5]
result = [n*2 for n in number if n%2==1]
print(result)