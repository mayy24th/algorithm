
from collections import deque

import sys
# [[3], [1], [1], [5], [5], [4], [6]]
# T F T F F F F

def dfs(start, v, visit):
    visit[v] = True
    for k in graph[v]:
        if not visit[k]:
            dfs(start, k, visit)
        elif visit[k] and k == start:
            res.add(k)

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i].append(int(input()))

res = set()
for i in range(1, N+1):
    visit = [False for _ in range(N + 1)]
    dfs(i, i, visit)

print(len(res))
for i in res:
    print(i)
