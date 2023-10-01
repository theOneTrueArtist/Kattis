n = int(input())
for _ in range(n):
    inp = input().split()
    x,y,w,h,r = [float(x) for x in inp[:5]]
    points = [(float(inp[x]), float(inp[x+1])) for x in range(6,len(inp),2)]
    r2 = r**2
    for point in points:
        if (point[0] >= x and point[0] <= x+w and point[1] >= y and point[1] <= y + h):
            if (point[0] >= x and point[0] <= x + r and point[1] >= y and point[1] <= y+r):
                if (point[0] - (x+r))**2 + (point[1] - (y+r))**2 <= r2:
                    print("inside")
                else:
                    print("outside")
            elif (point[0] >= x+w-r and point[0] <= x + w and point[1] >= y and point[1] <= y+r):
                if (point[0] - (x+w-r))**2 + (point[1] - (y+r))**2 <= r2:
                    print("inside")
                else:
                    print("outside")
            elif (point[0] >= x and point[0] <= x + r and point[1] >= y+h-r and point[1] <= y+h):
                if (point[0] - (x+r))**2 + (point[1] - (y+h-r))**2 <= r2:
                    print("inside")
                else:
                    print("outside")
            elif (point[0] >= x+w-r and point[0] <= x + w and point[1] >= y+h-r and point[1] <= y+h):
                if (point[0] - (x+w-r))**2 + (point[1] - (y+h-r))**2 <= r2:
                    print("inside")
                else:
                    print("outside")
            else:
                print("inside")
        else:
            print("outside")
    print()
        
