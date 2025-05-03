
#1. while loops
#2. for loops



#while loops
x=0
while (x<=5):
    print(x)
    x=x+1


#for loops
for x in range(5,10):
    print(x)


#Application of loops
#Arrays

days=["mon", "tue", "wed", "thur", "fri", "sat"]

for d in days:
    if (d=="wed"): break
    if (d=="thur"): continue
    print(d)


days=["mon", "tue", "wed", "thur", "fri", "sat"]

for d in days:
    if (d=="thur"): continue   #skips value in d
    print(d)