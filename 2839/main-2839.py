import sys

#f = sys.stdin
f = open('main-2839.txt','r')


N = int(f.readline().rstrip())
temp = N
result = -1


for i in range(0, N, 3):
  temp = N - i
  if temp % 5 == 0:
    result = (temp//5 + i//3)
    break

if result == -1:
  if N % 3 == 0:
    result = N // 3
print (result)