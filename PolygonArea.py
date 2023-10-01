def shoelace(poly):
    N = len(poly)
    fw = sum(poly[i - 1][0] * poly[i][1] for i in range(N))
    poly = list(reversed(poly))
    bw = sum(poly[i - 1][0] * poly[i][1] for i in range(N))
    return (fw - bw) / 2.0 

while (n:= int(input())) > 0:
    points = []
    for _ in range(n):
        points.append([int(x) for x in input().split()])
    area = shoelace(points)
    print("CW" if area < 0 else "CCW", abs(shoelace(points)))
