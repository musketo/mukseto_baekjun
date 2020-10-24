import sys



################ 재귀함수###############
# count=0
# def calc(sum, i):
#     global count
#     if n == i:
#         return
#     if sum + data[i] == s:
#         count += 1
#     calc(sum+data[i], i+1)
#     calc(sum, i+1)
########################################

#f = sys.stdin
with open('data.txt', 'r') as f:
    n, s = map(int, f.readline().split())
    data = list(map(int, f.readline().split()))

count = 0
stack = []
stack.append((0,0)) # sum, i
while stack:
    sum, i = stack.pop()
    print(sum,i)
    if i ==n:
        continue
    if sum + data[i] == s:
        count += 1
    stack.append((sum+data[i], i+1))
    stack.append((sum, i+1))

print(count)
