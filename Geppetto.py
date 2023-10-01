N, M = [int(x) for x in input().split()]

rules = [set() for x in range(N)]
for x in range(M):
    a, b = [int(x) for x in input().split()]
    rules[a-1].add(b-1)

num = 0
for x in range(1<<N):
    add = 1
    for a, _ in enumerate(rules):
        if add == 0:
            break
        for b in rules[a]:
            if x & (1 << a) and x & (1 << b):
                add = 0
                break
    num += add
print(num)
