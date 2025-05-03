x=10
y=10.2
z="hello"

print(type(x))
print(type(y))
print(type(z))

#implicit type conversion
x=x*y
print(x, "Type of x is, ", type(x) )

#Explicit type conversion
age=int(input("what is your age? "))
print(age, type(age))
