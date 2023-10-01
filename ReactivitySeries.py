from queue import deque
n, k = [int(x) for x in input().split()]
graph = {x: set() for x in range(n)}
outdeg = {x: 0 for x in range(n)}
indeg = {}
for x in range(k):
    A,B = [int(x) for x in input().split()]
    graph.setdefault(A,set()).add(B)
    outdeg[A] = outdeg.setdefault(A,0) + 1
    indeg[B] = indeg.setdefault(B,0) +1

startnode = -1
found = 0
possible = True
for x in range(n):
    if not x in indeg:
        startnode = x
        found+=1
if found != 1:
    possible = False

queue = deque([startnode])
topol = []
while len(queue) > 0 and possible:
    
    node = queue.popleft()
    topol.append(node)
    deleted = 0
    for nbr in graph[node]:
        indeg[nbr] -= 1
        if indeg[nbr] == 0:
            deleted += 1
            queue.append(nbr)
        if deleted == 2:
            possible = False
            break

if possible:
    for x in topol:
        print(x, end= " ")
    print()
else:
    print("back to the lab")
