num=int(input("Enter the number to check"))
sum=0
for i in range (1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("The number is a perfect number")
else:
    print("It is not a perfect number")
