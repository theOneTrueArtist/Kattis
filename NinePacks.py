import math
import sys
h = [int(x) for x in input().split()][1:]
b = [int(x) for x in input().split()][1:]
if len(h) == 0 or len(b) == 0:
    print("impossible")
    sys.exit()

W = max(sum(h),sum(b))

def minKnapsack01(val,W):
    dp = [[0 for j in range(W + 1)] for i in range(len(val))]
    for i in range(len(val)):
        for j in range(W):
            if (dp[i - 1][j] != 0):
                if dp[i-1][j + val[i]] != 0 and dp[i-1][j + val[i]][1] < dp[i-1][j][1] + 1:
                    dp[i][j + val[i]] = dp[i-1][j + val[i]]
                else:
                    dp[i][j + val[i]] = [dp[i-1][j][0] + val[i], dp[i-1][j][1] + 1]
                if not (dp[i][j] != 0 and dp[i][j][1] < dp[i - 1][j][1]):
                    dp[i][j] = dp[i-1][j]

        dp[i][val[i]] = [val[i],1]
    return dp[-1]

m = math.inf
for hi,bi in zip(minKnapsack01(h,W),minKnapsack01(b,W)):
    if hi != 0 and bi != 0:
        if hi[1] + bi[1] < m:
            m = hi[1] + bi[1]
print(m if m != math.inf else "impossible")
