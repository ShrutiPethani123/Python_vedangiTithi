'''
Take one number from user and print in words.

n - 245

two four five

n - 11679

one one six seven nine

'''

n = int(input("Enter a no: "))
rev=0
tmp=n

while(n!=0):
    rem=n%10
    rev=rev*10 + rem
    n=n//10

# print(rev)

res=" "
while(rev!=0):
    rem = rev%10
    if rem==1:
        res+=' one'
    elif rem==2:
        res+=' two'
    elif rem==3:
        res+=' three'
    
    rev = rev//10
    

print(res)
