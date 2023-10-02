#Q12-WAP to enter names of employees and their salariesas input and store them in a dictionary

dict1={}
num=int(input("Enter the number of employees:"))
for i in range(num):
    name=input("enter name of employee:")
    sal=int(input("Enter salary of employee:"))
    dict1[name]=sal
print(dict1)
    
