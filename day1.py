# -*- coding: utf-8 -*-
"""day1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EvAuD-dU51x_-1pC6eSFYu3-Y-dyjdGb
"""



"""varaible"""

a=5
print("I am",a,"years old")

"""operators"""

#arithmatic
a=5
b=25
print(a+b)

#power
print(2**3)

#floor division
print(25//5)

#relational
a=6
b=6
print(a==b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a!=b)

#logical
a=9
b=25
print((a>b) and (a<b))
print((a>b) or (a<b))

#membership
i="vijay"
print("i"not in i)
print("i"in i)



"""lists"""

#list
a=[]
for i in range(1,10,1):
  a.append(i)
print(a)

#max
l=[1,2,3,4,5]
print(max(l))

l.insert(1,7)
print(l)

#

#squares of list elements
l1=[2,3,4,5]
l2=[i**2 for i in l1]#[output iterator conition]
print(l2)

#squares of list elements
l1=[2,3,4,5]
l2=[i**2 for i in l1 if i>2]#[output iterator conition]
print(l2)

#the salries of 5 employes in company is taken as a list tax is 10% if the salary is less than =50k
#or it is 15%
#create a new list with tax amounts
#[67000,450000,89000,34000,50000]
#list_name=[(body of if) if (condition) else (body of else ) iterator]
sal=[67000,45000,89000,34000,50000]
tax=[i*0.1 if i<=50000 else i*0.15 for i in sal]
print(tax)

sal=[67000,45000,89000,34000,50000]
tax=[]
for i in sal:
  if (i>50000):
    t=(i*(15/100))
    tax.append(t)
  elif(i<=50000):
    t=(i*(10/100))
    tax.append(t)
print(tax)