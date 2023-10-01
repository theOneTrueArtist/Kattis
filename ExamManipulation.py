n, k = [int (x) for x in input().split()]
results = []

for _ in range(n):
    b = sum([2**i if x == "T" else 0 for i,x in enumerate(input())])
    results.append(b)

maxMin_ = 0
for x in range(1 << k):
    min_ = 1 << k
    for b in results:
        c = b ^ x

        bits = 0
        mask = 1
        for _ in range(k):
            if (c & mask) > 0:
                bits += 1
            mask <<= 1
 
        min_ = min(bits, min_)
    maxMin_ = max(min_, maxMin_)
 
print(maxMin_)
