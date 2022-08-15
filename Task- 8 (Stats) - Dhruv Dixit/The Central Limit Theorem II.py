import math
n = float(input())
nwait = float(input())
mean=float(input())
res= nwait*mean
std=float(input())
ans=math.sqrt(nwait) * std
print(round(0.5*(1+math.erf((n-res)/(ans * math.sqrt(2)))),4))