number=int(input("Enter the number to check"))
num_digits = len(str(number))
temp=number
sum=0
while temp>0:
    digit=temp%10
    sum+=digit ** num_digits
    temp=temp//10
if sum==number:
    print("The number is a armstrong number")  
else:
    print("Not an armstrong number")      