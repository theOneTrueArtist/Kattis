from queue import deque
n, m, c = [int(x) for x in (input().split())]
a = [int(x) for x in input().split()]

mx = deque([[a[0],0]])
mn = deque([[a[0],0]])

found = False
for i in range(1,n):
    if mx[0][1] + m == i:
        mx.popleft()
    
    if a[i] >= mx[0][0]:
        mx.clear()
        mx.append([a[i],i])
    elif len(mx) == 1:
        mx.append([a[i],i])
    else:
        l = len(mx)
        for _ in range(l):
            if a[i] >= mx[-1][0]:
                mx.pop()
                continue
            mx.append([a[i],i])
            break
    
    if mn[0][1] + m == i:
        mn.popleft()
    if a[i] <= mn[0][0]:
        mn.clear()
        mn.append([a[i],i])
    elif len(mn) == 1:
        mn.append([a[i],i])
    else:
        l = len(mn)
        for _ in range(l):
            if a[i] <= mn[-1][0]:
                mn.pop()
                continue
            mn.append([a[i],i])
            break
            

    if i > m-2 and mx[0][0] - mn[0][0] <= c:
        found = True
        print(i-m + 2)

if not found:
    print("NONE")
