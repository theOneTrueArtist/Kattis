import sys
import math as m

def f(n,w):
    if n > 1:
        if w: f(m.ceil(n/9),not w)
        else: f(m.ceil(n/2),not w)
    else:
        print("Ollie wins." if w else "Stan wins.")


for n in sys.stdin.readlines():
    n = int(n)
    f(n,True)
