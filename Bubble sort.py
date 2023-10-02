a = eval(input("Enter a list : "))
l = len(a)

for i in range(l):
     for j in range(l-i-1):
          if a[j] > a[j+1]:
               a[j],a[j+1] = a[j+1],a[j]
               
print("Sorted list : ",a)
