n=int(input("Enter the no of elements to be sorted"))
numbers=[]
for i in range(n):
    element=int(input(f"Enter the elements {i+1}:"))
    numbers.append(element)
print("\n Original list before sorting:",numbers)
for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if numbers[j]<numbers[min_idx]:
            min_idx = j 
    temp = numbers[i]
    numbers[i] = numbers[min_idx]
    numbers[min_idx]=temp 
print("Sorted list of the given numbers is :",numbers)