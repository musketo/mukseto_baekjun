import sys

f = sys.stdin
#f=open("data-1924.txt", "r")
M, D = map(int, f.readline().split())
day = D

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for m in range(1, 13):
    if m == M :
        break
    if m in [1,3,5,7,8,10,12]:
        day += 31
    elif m in [4,6,9,11]:
        day += 30
    else:
        day += 28

print(week[day%7])