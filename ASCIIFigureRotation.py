check = True
while True:
   
    if ((n := int(input())) == 0):
        break
    if not check:
        print()
    else:
        check = False
    lines=[]
    m = 0
    for x in range(n):
        lines.append([*input()])
        l = len(lines[x])
        if l > m:
            m = l
    for x in range(n):
        for y in range(len(lines[x])):
            if lines[x][y] == "-":
                lines[x][y] = "|"
            elif lines[x][y] == "|":
                lines[x][y] = "-"
        lines[x] += [" "] * (m - len(lines[x]))
    
    for line in list(zip(*lines[::-1])):
        print(("".join(line)).rstrip())
