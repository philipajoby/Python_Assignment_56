""" Write a python program to find the factorial of a number entered by the
user using a while loop"""

num=int(input("Enter a number:"))
f=num
if f==0:
    print("The factorial of 0 is 1")
else:
    fact=1
    while f>1:
      fact=fact*f
      f=f-1
print(f"The factorial of the number {num} is: {fact}")
