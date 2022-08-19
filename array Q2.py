''''program to reverse the items of the order in the array'''

import array as arr
a=arr.array('i',[1,2,3,4,5])
print("The element of array are")
for i in range(0,5):
   print(a[i])
a.reverse()
print("The element of array are")
for i in range(0,5):
   print(a[i])
