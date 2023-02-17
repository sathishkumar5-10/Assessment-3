#!/usr/bin/env python
# coding: utf-8

# write a program to enter two number and print the greatest number.

# In[2]:


a=int(input("Enter the A value"))
b=int(input("Enter the B value"))
if(a>b):
    print(a,"is greatest number")
else:
    print(b,"is greatest number")


# write a program to enter two number and print the smallest number.

# In[3]:


a=int(input("Enter the A value"))
b=int(input("Enter the B value"))
if(a>b):
    print(b,"is smallest number")
else:
    print(a,"is smallest number")


# write a program to enter three number and print the greatest number

# In[10]:


a=int(input("Enter the A value"))
b=int(input("Enter the B value"))
c=int(input("Enter the C value"))
if(a>b and c):
    print(a,"is greatest number")
elif(b>c and a):
    print(b,"is greatest number")
elif(c>b and a):
    print(c,"is greatest number")


# write a program to enter three number and print the smallest number

# In[26]:


a=int(input("Enter the A value"))
b=int(input("Enter the B value"))
c=int(input("Enter the C value"))
if(a<b and a<c):
    print(a,"is smallest number")
elif(b<c and b<a):
    print(b,"is smallest number")
else:
    print(c,"is smallest number")


# root of quadratic equation

# In[29]:


a=int(input("Enter the value"))
b=int(input("Enter the value"))
c=int(input("Enter the value"))
d=(b**2-4*a*c)**(.5)
print((-b+d)/2*a),((-b-d)/2*a)


# write a program to enter no between (1 to 7) and display respective days in a week

# In[38]:


day=int(input("enter the day in a week"))
if(day==1):
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Wednesday")
elif(day==4):
    print("Thursday")
elif(day==5):
    print("Friday")
elif(day==6):
    print("Saturday")
elif(day==7):
    print("Sunday")


# In[ ]:





# In[ ]:




