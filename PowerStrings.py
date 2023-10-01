while not (line:=input()) == ".":
    match = [0] * len(line)
    i,j = 1,0
    while i < len(match):
        if line[i] == line[j]:
            match[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            match[i] = 0
            i += 1
        else:
            j = match[j-1]

    print(len(line) // (len(line) - match[-1]))
