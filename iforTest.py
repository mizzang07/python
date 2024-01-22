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
"""
c = [[1,2,3],[4,5,6],[7,8,9]]
for j in range(len(c)) :
    for k in range(len(c[j])) :
        print(c[j][k])
