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