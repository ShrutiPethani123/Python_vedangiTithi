# for i in range(1,5): # 1
#     for j in range(1,6):
#         print(i,j)

# for i in range(2,7):
#     j=1
#     while j<=5:
#         print(i,j)
#         j+=2

'''
* * * * *
* * * * *
* * * * *
* * * * *

'''

for i in range(4):
    for j in range(5):
        print('*',end=" ")
    print()


'''
1. 

1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

2. 

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20

3.

1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16

4.

1
12
123
1234

5. 

1
2 3
4 5 6
7 8 9 10

6.

*
**
* *
*  *
*****


'''

# 3.
# for i in range(1,5):
#     for j in range(1,5):
#         print(i*j,end=" ")
#     print()

# 3.
for i in range(1,5):
    k=i
    for j in range(1,5):
        print(k,end=" ")
        k=k+i  
    print()


