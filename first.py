# comment single line 


c= '''
multi
line
comment

'''
print(c)

print("Hello Good Morning!!")
print('java','python')
print('java'+'python')

# Hello I have "big" sister's

print("Hello I have \"big\" sister\'s")

print("java",end="123")
print("python")

print('java \t python')

'''
\n
\t
\'
\"
\\
\\\

'''

# Data types:
'''
int
float
str
bool
complex

'''

# a=234
a=-56468468468486416548946541986546876846468
print(a)
print("Vale of a: ",a)
print(type(a))

a=45.343422345325214
print(a)
print("Vale of a: ",a)
print(type(a))

# a="Python"
a='h'
print(a)
print("Vale of a: ",a)
print(type(a))


# a=True
a=False
print(a)
print("Vale of a: ",a)
print(type(a))

a=2+4.88j
print(a)
print("Vale of a: ",a)
print(type(a))
print("Real: ",a.real)
print("Imag: ",a.imag)

'''
complex = real+ imag

real: 2
imag: 4
'''

'''
Type Casting


int()
str()
float()
bool()
complex()
'''

n = 655.654
# n=float(n)
print(n , type(n))

c = float(n)
print(c,type(c))

d=str(n)
print(d,type(d))

d=bool(n)
print(d,type(d))

d=complex(n,45)
print(d,type(d))

b = False
c=True
print(float(b))

s='abc'
print(complex(c,b))