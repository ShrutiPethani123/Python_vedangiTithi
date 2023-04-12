'''

3,5 : 1

6 : 1 2 3 6 
12 : 1 2 3 4 6 12

hcf/gcd: 6

'''

a = int(input("Enter a no: "))
b = int(input("Enter a no: "))


if a<b:
    min=a
else:
    min=b

i=1
while(i<=min):
    if(a%i==0 and b%i==0):
        hcf=i
    i+=1

print(f"hcf of {a} and {b} is {hcf}")
