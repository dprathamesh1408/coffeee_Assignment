'''Program to add ing at the end of a given string (length should be at least 3).If the given string already ends with ing then add ly instead .if the string length of the given string os less than 3 ,then leave it unchanged.'''

s=input("Enter a string\n")
l=len(s)
if (l>=3):
    if(s.endswith("ing")):
        s=s+"ly"
    else:
        s=s+"ing"  

print("The new string is \n",s)   
