def findPairSum(node, used):
    if DP.get(node) and DP[node].get(used):
        return DP[node][used]

    pairs = 0
    num = 0
    for child in tree[node]:
        child_pairs, child_num = findPairSum(child, False)
        pairs += child_pairs
        num += child_num

    maxPair = (pairs, num)

    if not used:
        for child in tree[node]:
            f_pairs, f_num = findPairSum(child, False)
            t_pairs, t_num = findPairSum(child, True)
            pairs_ = pairs - f_pairs + 1 + t_pairs
            num_ = num - f_num + min(speeds[child], speeds[node]) + t_num

            maxPair = max(maxPair, (pairs_, num_))

    if not node in DP:
        DP[node] = {}
    DP[node][used] = maxPair
    
    return maxPair

n = int(input())

speeds = {}
tree = {}
DP = {}

for i in range(n):
    child, speed, parent = input().split()
    speeds[child] = float(speed)
    if not child in tree:
        tree[child] = []
    if not parent in tree:
        tree[parent] = []
    tree[parent].append(child)

maxPairSum = findPairSum("CEO", True)
print(maxPairSum[0], maxPairSum[1]/maxPairSum[0])
