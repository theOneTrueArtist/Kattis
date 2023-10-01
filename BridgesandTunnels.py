n = int(input())

parents = {}
sizes = {}

def find(node):
    if node not in parents:
        parents[node] = node
        sizes[node] = 1
    elif parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2:
        print(sizes[root1])
    else:
        if sizes[root1] > sizes[root2]:
            root1, root2 = root2, root1
        parents[root1] = root2
        sizes[root2] += sizes[root1]
        print(sizes[root2])

for i in range(n):
    node1, node2 = input().split()
    union(node1, node2)
