i=input
p=sorted([i().split()for(_)in range(int(i()))])
print(max([abs(eval(i[1]+"-"+j[1]))/abs(eval(i[0]+"-"+j[0]))for(i,j)in zip(p[:-1],p[1:])]))
