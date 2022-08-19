'''program to create a symmetric difference'''

s1={1,2,3,4,5}
s2={3,4,5,6,7}
print("set1--\n",s1)
print("set2--\n",s2)
s=set()
s=s1.symmetric_difference(s2)
print("symmetric difference of set1 and set2 is--\n",s)
