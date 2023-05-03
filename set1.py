'''

set:  {}


'''

s1={2,3,4,5,1,6,7}
print(s1)

s2={34,56,12,78,12,4,89,345,4,4,4,1,5,6,12,56}
print(s2)

print(len(s1))
print(max(s2))
print(min(s2))

s2.add(100)
print(s2)

s2.update(s1)
print(s2)

s2.update([200,300,400,500])
print(s2)

s3 = s2.copy()
print(s3)

s3.remove(300)
print(s3)

s4=s2
s4.remove(500)

print(s2)

print(s2.pop())
print(s2.pop())

print(s2)

del s3
s4.clear()
print(s4) #[] () set() {}

s1={1,2,3,4}
s2={3,4,5,6}

s3 = s1.union(s2)
print(s3)

print(s1.intersection(s2))
print(s1)

# s1.intersection_update(s2)
# print(s1)

print(s1.difference(s2))

# s1.difference_update(s2)
# print(s1)

print(s1.symmetric_difference(s2))

# s1.symmetric_difference_update(s2)
# print(s1)


l=[2,3,1,4,1,4,5,2,6,1,3,9]
s=set(l)
l2=list(s)
print(l2)

