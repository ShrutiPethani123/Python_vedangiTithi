'''

lcm:

5 - 5 10 15 20 25 30 35 ....
6 - 6 12 18 24 30 36 ....

lcm: 30


4: 4 8 12 16
8: 8 16 24

lcm: 8

'''

a = int(input("Enter a no: "))
b = int(input("Enter a no: "))


if a<b:
    max=b
else:
    max=a

i=max
count=0
while(True):

    if(i%a==0  and i%b==0):
        lcm=i
        break

    i+=max
    count+=1

print(f"LCM of {a} and {b} is {lcm} ----> {count}")




