#Python Program to Calculate Average of Numbers:

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
elem=int(input("Enter element: "))
a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))


"""
Output:
Enter the number of elements to be inserted: 3
Enter element: 23
Enter element: 45
Enter element: 56
Average of elements in the list 41.33

"""