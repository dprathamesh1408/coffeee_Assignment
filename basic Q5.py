'''program to print the calender of given month and year'''

from calendar import calendar, monthcalendar
i=int(input("Enter a year \n"))
m=int(input("Enter a month\n"))
print(monthcalendar(i,m))
