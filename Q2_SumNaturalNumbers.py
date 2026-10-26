""" write a python program to calculate the sum of the first N natural numbers
using a for loop.The user should input N."""

sum=0
num=int(input("Enter the first N natual number:"))
for i in range(1,num+1):
    sum=sum+i
print(f"The sum of the first N natural number is:{sum}")
    
