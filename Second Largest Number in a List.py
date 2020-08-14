#Python Program to Find the Second Largest Number in a List:

a=[]
n=int(input("Enter number of elements:"))
  for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
    a.sort()
     print("Second largest element is:",a[n-2])


"""
Output:

Enter number of elements:3
Enter element:23
Enter element:56
Enter element:39
Second largest element is: 39
"""
