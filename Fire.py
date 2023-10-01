
from collections import deque
#O(f^2)
def progressFires(room,flames):
    l = len(flames)
    #O(f)
    for i in range(l):
        pos = flames[0]
        neighbors = [[pos[0]+x,pos[1]] for x in [-1,1]] + [[pos[0],pos[1]+x] for x in [-1,1]]
        #O(4f)
        for nbr in neighbors:
            if nbr[0] in [-1, h] or nbr[1] in [-1, w]:
                continue

            if room[nbr[0]][nbr[1]] == "." or room[nbr[0]][nbr[1]] == "@":
                room[nbr[0]][nbr[1]] = "*"
                flames.append([nbr[0],nbr[1]])
        flames.popleft()

cases = int(input())

for x in range(cases):
    w, h = [int(x) for x in input().split()]
    room = []
    startpos = [0,0]
    flames = deque([])
    #o(hw)
    for i in range(h):
        room.append([*input()])
        #o(w)
        for j in range(len(room[i])):
            if room[i][j] == "@":
                startpos = [i, j]
            if room[i][j] == "*":
                flames.append([i,j])
    #O(hw)
    distance = [[-1 for x in range(w)] for y in range(h)]
    distance[startpos[0]][startpos[1]] = 0
    dequeue = deque([startpos]) 
    possible = False
    count = -1
    #O()
    while len(dequeue) > 0:
        #O(1)
        pos = dequeue.popleft()
        if distance[pos[0]][pos[1]] > count:
            count += 1
            #O(f^2)
            progressFires(room,flames)

        if pos[0] in [0, h-1] or pos[1] in [0,w-1]:
            print(distance[pos[0]][pos[1]] +1)
            possible = True
            break

        neighbors = [[pos[0]+x,pos[1]] for x in [-1,1]] + [[pos[0],pos[1]+x] for x in [-1,1]]
        for nbr in neighbors:
            if distance[nbr[0]][nbr[1]] ==-1 and room[nbr[0]][nbr[1]] == ".":
                distance[nbr[0]][nbr[1]] = distance[pos[0]][pos[1]] + 1
                dequeue.append(nbr)
    

    if not possible:
        print("IMPOSSIBLE")
