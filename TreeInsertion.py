import math

def countBSTs(nodes):
    if (len(nodes) < 3):
        return 1
 
    left, right = [], []

    [(lambda lst, node: lst.append(node))(left if nodes[i] < nodes[0] else right, nodes[i]) for i in range(1, len(nodes))]
 
    return (math.comb(len(nodes) - 1, len(left)) * countBSTs(left) * countBSTs(right))

while int(input()) != 0:
    nodes = [int(x) for x in input().split()]
    print(countBSTs(nodes))
