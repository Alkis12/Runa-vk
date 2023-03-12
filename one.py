for i in range(700):
    print(i)
import datetime as dt

d1, d2 = input().split()
d1 = d1.split('-')
d1 = dt.date(int(d1[0]), int(d1[1]), int(d1[2]))
d2 = d2.split('-')
d2 = dt.date(int(d2[0]), int(d2[1]), int(d2[2]))
k = int(input())
anss = []
while d1 != d2:
    d1 += dt.timedelta(days=1)
    if d1.day % k != 0 and d1.strftime("%w") != 2:
        anss.append(d1)
        if len(anss) == 3:
            for i in anss:
                print(i.strftime("%d %B %Y, %a"))
            break
else:
    print('CANCEL CARNIVAL')
