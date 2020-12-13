# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:48:30 2020

@author: shrey
"""

import pytesseract
from PIL import Image#PIL- PYTHON IMAGING LIBRARY
import matplotlib.pyplot as plt

img=Image.open('zoom-class9.png')
text=pytesseract.image_to_string(img, config='')

p=[]

s=""
a=text.split(' ')

for item in a:
    k=item.replace('\n',' ')
    m=k.replace('.',' ')
    p.append(m.casefold())
s=' '.join(p)

print("which class' attendance are you taking?")
u=input()
if u=='9':
    f=open('class 9 student list.txt')#files
if u=='8':
    f=open('class 8 student list.txt')


l=[]
absentees=[]

for i in f:
    k=i.replace('\n','')
    l.append(k.casefold())
    
f.close()

avoid=['9-opal','9-sapphire','9-ruby', '8-opal','8-sapphire','8-ruby']
print("absentees are")

for i in range(len(l)):
    
    if l[i] in avoid:
        print("\n")
    
    if l[i] not in s:
        
        print(l[i])
        
        absentees.append(l[i])

if u=='9':
    f=open('attendance of class 9.txt','a')
    for i in range(len(absentees)):
        f.write(absentees[i])
        f.write("\n")
f.close()

if u=='8':
    f=open('attendance of class 8.txt','a')
    for i in range(len(absentees)):
        f.write(absentees[i])
        f.write("\n")
f.close()


absentfile=[]
if u=='9':
    f=open('attendance of class 9.txt','r')
    for line in f:
        k=line.replace('\n','')
        absentfile.append(k)
f.close()
if u=='8':
    f=open('attendance of class 8.txt','r')
    for line in f:
        k=line.replace('\n','')
        absentfile.append(k)
f.close()

record={}
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

for i in range(len(absentfile)):
    if absentfile[i] not in avoid:
        a=absentfile.count(absentfile[i])
        
        record[absentfile[i]]=a
ke=list(record.keys())
val=list(record.values())


val2=[]
ke2=[]
print("\n do you want to know who is frequently absent in class?")
ans=input()
if ans=='yes':
    a=input("enter the no. of days")
    
    plt.title(str('students absent for ' +a+' or more days'))
    plt.xlabel('names of students')
    plt.ylabel('days absent')
    for i in range(len(val)):
        if val[i]>=int(a):
            val2.append(val[i])
            ke2.append(ke[i])
ax.bar(ke2,val2)

plt.show()
