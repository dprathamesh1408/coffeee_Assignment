'''Program to concatenate all elements in a list into a string and return it '''

l=['a','b','c','d','e','f']
print(l)
s=""
for i in range(0,len(l)):
    s+=str(l[i])
print(s)
