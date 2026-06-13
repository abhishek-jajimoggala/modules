'''Difference between module,library and package
module:
----------
A module in python is a single python file it consist of python program.
*it typically functions,classes and variables that can be used in other python scripts or programs.
* Example of modules include math.py,random.py or mymodule.py

Package:
---------
A package in python is a directory containing 1 or more python modules and an __init__.py file.
It file is empty or contain initialization code for the package.
Ex of packages include numpy,pandas,or Django


library:
---------
it consist of multiple modules and packages,organized to serve a particular purpose or domain.
Ex of library such as request,numpy,pandas and matplotlib.

Note:
-----
Every python file is a module and import is keyword and every python file is saved internally with variable name as
__main__'''

'''def greetings(name):
    print("Welcome",name)'''

'''a=10
b=3
print(a+b)'''

'''a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print(a*b)'''

'''details={'idnos':[10,20,40,50],
         'names':["abhishek","rohith","baskar","rakshit"],
         'cities':["vijayawada","vizag","banglore"]}'''

'''if __name__=="__main__":
    a=[10,30,20,50]
    #a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("This program is from script")
    else:
        print("This program is from a module")
dummy()'''

#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.log(2))
print(math.sin(30))
print(math.cos(60))
print(math.tan(20))
print(pow(2,4))
print(math.ceil(2.8))
print(math.floor(4.8))
print(math.sqrt(4))'''

'''from math import pi,sqrt,log
print(pi)
print(sqrt(3))
print(log(4))'''

'''n=int(input())
for i in range(1,21):
    print(n,"x",i,"==",n*i)'''
#sys module(system module)
'''import sys
print(sys.path)

for i in sys.path:
    print(i)

print(sys.version)'''

#os module
'''import os
print(os.O_RANDOM)#random
print(os.path)#path
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\ABHISHEK\\Downloads"))
print(os.listdir())'''

#random module
'''random module:To generate a random number in python,randint() is used is defined in random module.
python define a set of function generate or mainipulate random numbers through the random module.'''
#import random
'''a=random.sample(range(1,100),50)
print(a)
print(random.randint(10,50))'''

'''import random
a=[10,20,40,50,30,100,90,80]
b=random.choice(a)
print(b)'''

#dice game
'''import random
while True:
    roll_dice=int(input("Enter the any number:"))
    print(random.randint(1,roll_dice))
    print("Choose your options:1.yes 2.No")
    choice=int(input("Choose your option:y"))
    if choice==1:
                  continue
    else:
        break'''

#calendar module
'''import calendar
year=2026
month=6
print(calendar.month(year,month))'''

'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
year=int(input())
print(calendar.calendar(year))'''

'''import calendar
year=int(input())
month=int(input())
print(calendar.month(year,month))'''

#time and date
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
#print(a)
b=time.localtime()
print(b)
print(f"Today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"Year of the time is:{b.tm_year},Hour is:{b.tm_hour},minutes is {b.tm_min},Seconds is:{b.tm_sec}")
print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''


#Regular Expression are powerful tools and embedded systemswe mainly used for text manipulations.


#regex()regular expression
'''a="codegnan\nit\tsolutions"
print(a)

#rstring
a=r"codegnan\nIt\tsolutions"
print(a)'''

#compile(),split(),findall(),search(),sub()
#sequence characters
'''
\w->it matches alphanumeric
\W->it matches non alphanumeric
\d->it matches any digit
\D->it matches non digit
\s->It represents white spaces
\S->It represents non white spaces'''

import re
#a="map cat dog maths money cash cap cup mug donkey"
'''b=re.compile(r"m\w\w\w")
print(b)'''

'''c=b.search(a)
print(c)'''

'''d=re.search(r"m\w+",a)
print(d)'''

#findall()
'''d=re.findall(r"m\w+",a)
print(d)
d=re.findall(r"m\w+",a)
print(*d)
e=re.findall(r"d\w+",a)
print(e)
f=re.findall(r"c\w+",a)
print(f)
print(a)'''

#split()
'''e=re.split(r"m",a)
print(e)
f=re.split(r"\s",a)
print(f)'''

#sub()
'''x=re.sub(r"maths","science",a)
print(x)
x=re.sub(r"m","a",a)
print(x)'''

s="1 2 4 5 6 7 8 10 11 14 25 13 15"
print(re.findall(r"1\d",s))

a="year 2026 month 6 date 13"
b=re.findall(r"\d",a)
print(b)
b=re.findall(r"\d+",a)
print(b)








      














