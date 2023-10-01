c = int(input())
for _ in range(c):
    d, n = [int(x) for x in input().split()]
    seq = [int (x) for x in input().split()]
    tot = 0

    prefix = [seq[0]]
    for i in range(1,len(seq)):
        prefix.append(prefix[i-1]+seq[i])
    
    modprefix = [((prefix[x] % d) + d) % d for x in range(len(prefix))]

    vals = {}
    for x in (modprefix):
        vals[x] = vals.setdefault(x,0) + 1

    for v in vals:
        if vals[v] > 1:
            tot += (vals[v] *(vals[v]-1))/2
    tot += vals.setdefault(0,0)
    print(int(tot))
