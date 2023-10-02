tup=eval(input("enter a tuple of 10 no.:"))
tup1=()
for i in tup:
    for j in range(2,i):
        if i%j==0:
            break
        
    else:
        tup1+=(i,)
print(tup1)
