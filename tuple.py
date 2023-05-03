# tuple : immutable and ordered


t1=('india','china','japan','france')
print(t1 , type(t1))

t=(3)
t=('java')
t=('java',)
print(t , type(t))


t2=(12,34,'java',45.4455,True)

print(t2)
print(len(t1))
print(min(t1))
print(max(t1))

t1=('india','china','UK','japan','france','UK','USA','Singapor','UK')
print(t1)
print(t1[3])
# t1[3]="germany"
print(t1[1:4])
print(t1[-2:-9:-1])
print(t1[::-1])

l1 = list(t1)
l1.append("Bhutan")
t1 = tuple(l1)
print(t1)


for i in t1:
    print(i)


str="royal"
print(str*2)

print(t1*2)

t2=(1,2,3,4,5)
print(t1+t2)

# count , index

print(t1.index('india'))
print(t1.index("UK"))
print(t1.index("UK",3))

print(t1.count('UK'))
print(t1.count('UK1'))


