import math
max_weight=int(input())
n=int(input())
mean_weight=int(input())
std=int(input())
s=n*mean_weight 
ssum = math.sqrt(n) * std
def solve(x,y,z):
    res= (x-y)/z
    return 0.5*(1 + math.erf(res/(math.sqrt(2))))
print(round(solve(max_weight,s,ssum), 4))