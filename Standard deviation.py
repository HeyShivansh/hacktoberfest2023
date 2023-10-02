from math import sqrt as sq

samp = (1,2,3,4,5,6,7,8,9,10)
n = len(samp)
s,s2=0,0
for i in range(n):
    s+=samp[i]
x_mean = s/n
print("Mean",x_mean)

for i in range(n):
    s2 += (samp[i]-x_mean)**2
print("Variance",s2)

SD = sq(s2/(n-1))

print("Standard deviation",SD)
