def dfs(node,color):
    if (node,color) in DP:
        return DP[(node,color)]
    num = 0
    for nbr in edges[node]:
        if not colors[nbr] & color:
            num += dfs(nbr, colors[nbr] + color) + 1
    DP[(node, color)] = num
    return num

DP = {}
n,k,m = [int(x) for x in input().split()]
colors = [2**int(c) for c in input().split()]
edges = [set() for x in range(n)]
for x in range(k):
    a, b = [int(x)-1 for x in input().split()]
    edges[a].add(b)
    edges[b].add(a)
num = 0
for node in range(n):
    num += dfs(node, colors[node])
print(num)
