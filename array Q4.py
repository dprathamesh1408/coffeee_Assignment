'''Program to remove first occurence of a specified element in the array'''

import array as arr
a=arr.array('i',[1,1,3,4,5])
a.remove(1)
print("The element of array are")
for i in range(0,5):
    print(a[i])
