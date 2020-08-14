#Python Program to Reverse a Number:

n=int(input("Enter number: "))
rev=0
 while(n>0):
   dig=n%10
   rev=rev*10+dig
   n=n//10
   print("The reverse of the number:",rev)



"""
OUTPUT:
Enter number: 143
The reverse of the number: 341
"""