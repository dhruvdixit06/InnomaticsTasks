import math
mean, std = 70, 10
def solve(x):
    ans=0.5*(1+math.erf((x-mean)/(std*(2**0.5))))
    return ans
print(round((1-solve(80))*100,2))
print(round((1-solve(60))*100,2))
print(round((solve(60))*100,2))