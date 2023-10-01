from collections import deque

def create_path(parent, s, t):
    path = [t]
    while t != s:
        t = parent[t]
        path.append(t)
    return tuple(reversed(path))

def bfs(graph, s, t):
    q = deque([s])
    parent = {}
    while q:
        v = q.popleft()
        for u, cap in enumerate(graph.R[v]):
            if u in parent:
                continue # seen it before
            if cap <= 0:
                continue # vu saturated
            parent[u] = v
            q.append(u)
            if u == t:
                return create_path(parent, s, t)


def maxflow(graph, s, t):
    flow = 0
    while True:
        P = bfs(graph, s, t)
        if P is None:
            break
        F = min(graph.R[v][u] for (v, u) in zip(P, P[1:]))
        flow += F
        for v, u in zip(P, P[1:]):
            graph.R[v][u] -= F
            graph.R[u][v] += F
    return flow

class Graph:
    def __init__(self, n):
        self.V = list(range(n)  )
        self.R = [[0]*n for _ in range(n)]

n, m, p = [int(x) for x in input().split()]
children = []
categories = []
for _ in range(n):
    children.append([int(x)-1 for x in input().split()][1:])
for _ in range(p):
    categories.append([int(x)-1 for x in input().split()][1:])

for i in range(len(categories)):
    categories[i][-1] += 1

graph = Graph(n+m+p+2)
S = n+m+p
T = n+m+p+1

for i in range(n):
    graph.R[S][i] = 1

for i in range(n):
    for j in range(m):
        if j in children[i]:
            graph.R[i][n+j] = 1

for i, cat in enumerate(categories):
    for toy in cat[:-1]:
        graph.R[n+toy][n+m+i] = 1
    graph.R[n+m+i][T] = cat[-1]

for j in range(m):
    incat = False
    for i in range(p):
        if graph.R[n+j][n+m+i]:
            incat = True
    if not incat:
        graph.R[n+j][T] = 1

print(maxflow(graph, S, T))

