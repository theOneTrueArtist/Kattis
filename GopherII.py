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
    return None

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
        self.V = list(range(n))
        self.R = [[0]*n for _ in range(n)]

def distance(x1, y1, x2, y2):
    return (x2-x1)**2 + (y2-y1)**2

def can_reach(x1, y1, x2, y2, s, c):
    d_squared = distance(x1, y1, x2, y2)
    return d_squared <= (s * c) ** 2

while True:
    try:
        n,m,s,c = [int(x) for x in input().split()]
        gophers = []
        for _ in range(n):
            x, y = [float(x) for x in input().split()]
            gophers.append((x, y))
        holes = []
        for _ in range(m):
            x, y = [float(x) for x in input().split()]
            holes.append((x, y))

        graph = Graph(n+m+2)
        S = n+m
        T = n+m+1

        for i in range(n):
            graph.R[S][i] = 1

        for i in range(n):
            for j in range(m):
                if can_reach(gophers[i][0], gophers[i][1], holes[j][0], holes[j][1], s, c):
                    graph.R[i][n+j] = 1

        for j in range(m):
            graph.R[n+j][T] = 1

        max_flow = maxflow(graph, S, T)

        print(n - max_flow)

    except EOFError:
        break
