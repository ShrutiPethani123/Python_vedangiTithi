'''

string : ordered  immutable --> ' ' or " "
list : ordered  mutable --> []
tuple : ordered  immutable --> ()
set : unordered  mutable --> {}
dictionary: unordered  mutable --> {key:value}

'''


l1=[1,2,3,4,5]
print(l1)

l1=[1,2,4.55,2.789,"java",'python',True]
print(l1)

print(type(l1))

# iterate the list

for i in l1:
    print(i , type(i))
print(l1[3])
print(l1[-2])
print(l1[-4])

# slicing
print(l1[2:])
print(l1[:3])
print(l1[2:6])
print(l1[2:6:2])
print(l1[:])
print(l1[:: -1])
print(l1[-2:-5])
print(l1[-2:-5:-1])
print(l1[-5:-2])
print(l1[1:-3])
print(l1[-3:1:-1])


l3=[1,4,1,5,72,7]

for i in l3:
    print(i)

for i in range(0,len(l3)):
    print(l3[i],end=" ")

print()

print(len(l3))
print(max(l3))
print(min(l3))
print(sum(l3))
print(sorted(l3))
print(sorted(l3,reverse=True))
print(l3)

# l3.sort()
# l3.sort(reverse=True)
# print(l3)

l4=['apple','kiwi','banana','orange','mango']
print(l4)
print(len(l4))
print(max(l4))
print(min(l4))
print(sorted(l4))
print(sorted(l4,reverse=True))

