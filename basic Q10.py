'''Program to print out a set containing all the colours from color_list_1 which are not present in color_list_2'''

color_list_1=set(["White","Black","Red"])
color_list_2=set(["Red","Green"])
s=set()
s=color_list_1.difference(color_list_2)
print("The set containing all the colours from set1 which are not in set2  \n",s)
