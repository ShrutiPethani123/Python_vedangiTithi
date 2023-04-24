# user input

# l=[]
# n=int(input("Enter length: "))

# for i in range(n):
#     l.append(int(input("Enter element: ")))

# print(l)

l2=[3,9,90,5,2,78,9]

l3=l2.copy()
print(l3)

l4=l2
print(l4)

print(id(l2))
print(id(l3))
print(id(l4))

l4.append(100)
print(l2)

l3.append(300)
print(l2)

print(l3 is l2)
print(l4 is l2)

print(l3 is not  l2)
print(l4 is not l2)  

l3.clear()
print(l3)

# del l3
# print(l3)

print(l2)

print(30 in l2)
print(9 in l2)

print(l2.index(9))
print(l2.index(9,4))
print(l2.index(9,2,8))
# print(l2.index(55)) - error

l2.append(300)
print(l2)
l2.insert(3,5000)
print(l2)

l4=[5,6,7]
l2.append(l4)
print(l2)
l2.extend(l4)
print(l2)


print(l2.count(9))
print(l2.count(80))

l2[0]=56
print(l2)

print(l2.pop(3))
print(l2)

l2.remove(100)
print(l2)




