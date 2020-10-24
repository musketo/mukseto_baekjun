#그래프와 배열 , 그래프와 리스트


import sys
import queue

#f=sys.stdin
lines=[]
visit=[]
with open('virus.txt', 'r') as f:
computer_cnt = int(f.readline())
for i in range(computer_cnt+1):
    lines.append([])
    visit.append(0)
    
line_cnt = int(f.readline())
for i in range(line_cnt):
    src, dst = list(map(int, f.readline().split()))
    lines[src].append(dst)
    lines[dst].append(src)

q = queue.Queue()
q.put(1)
while not q.empty():
    src = q.get()
    if visit[src] == 1:
        continue
    else:
        visit[src] = 1

    for dst in lines[src]:
        q.put(dst)

count = 0
for i in range(2, computer_cnt+1):
    if visit[i] == 1:
        count +=1
print(count)