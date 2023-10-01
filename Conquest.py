from queue import PriorityQueue

N,M = [int(x) for x in input().split()]

graph = {i:[] for i in range(1,N+1)}
weight = []
for i in range(M):
    b1,b2 = [int(x) for x in input().split()]
    graph[b1].append(b2)
    graph[b2].append(b1)

for j in range(N):
    weight.append(int(input()))

visited = {1}

def putEdges(prique, i):
    for b in range(len(graph[i])):
        if graph[i][b] in visited:
            continue
        prique.put((weight[graph[i][b]-1], graph[i][b]))

pq = PriorityQueue(M)
putEdges(pq,1)
army = weight[0]
while not pq.empty():
    edge = pq.get()
    if army <= edge[0]:
        break
    if edge[1] in visited:
        continue
    visited.add(edge[1])
    putEdges(pq, edge[1])
    army += edge[0]
    
print(army)
