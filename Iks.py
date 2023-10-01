import math
from collections import defaultdict

def primeFactors(n,prims):
    factors = defaultdict(int)
    while n % 2 == 0:
        prims[2] += 1
        factors[2] += 1
        n = n / 2
         
    for i in range(3,int(math.sqrt(n))+1,2):         
        while n % i== 0:
            prims[i] += 1
            factors[i] += 1
            n = n / i
             
    if n > 2:
        prims[n] += 1
        factors[n] += 1
    return factors
 
n = int(input())

primes = defaultdict(int)
factors = [primeFactors(int(num), primes) for num in input().split()]

for i in primes:primes[i] //= n

gcd = math.prod([i**primes[i] if primes[i] != 0 else 1 for i in primes])
operations = sum([max(0, primes[j] - i[j]) for j in primes for i in factors])

print(int(gcd), operations)
