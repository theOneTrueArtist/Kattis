import math

def angle(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.atan2(dy, dx)

def simple_polygon(points):
    p0 = (sum([p[0] for p in points])/len(points), sum([p[1] for p in points])/len(points))
    angles = [(angle(p0, p), p) for p in points]
    return [x[1] for x in sorted(angles)]

c = int(input())

for _ in range(c):
    n, *coords = map(int, input().split())
    
    points = [(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]
    
    order = {point : str(i) for i,point in enumerate(points)}

    polygon = simple_polygon(points)
    p = ""
    for point in polygon:
        p += order[point] + " "
    print(p[:-1])
