no= int(input("Enter the number(between 10 and 99):"))
X=["","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
X1=["","one","two","three","four","five","six","seven","eight","nine"]
X2=["","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
a=no%10
b=no//10
if b!=1:
    print(X2[b-1]+""+X1[a])
else:    print(X[no-9])