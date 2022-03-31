#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=int(input("Enter the value of X\n"))
f=False
for i in range(1,x+1,1):
    if x % i == 0:
        f=True
        
if f==1:
    print(x,"in not prime number")
else:
    print(x,"is a prime number")


# In[ ]:


#Task 02

x=int(input("Enter the value of X\n"))
y=x%10
if y%2==0:
    print(y,"last disgit is even")
else:
    print(y,"last disgit is odd")


# In[ ]:


#Task 03

x=int(input("Enter the value of X\n"))

even=0
odd=0
i=0
for i in range(i,x,1):
    if x%2==0:
        even+=1
    else:
        odd++1
        
print (even,"are even number and ",odd,"are odd numbers")


# In[1]:


x=int(input("Enter the value of X\n"))
ev=od=rem=0
while x != 0:
    rem=x%10
    if rem%2==0:
        ev=ev+1
    else:
        od=od+1
        
    x=x//10
print (ev,"are even number and ",od,"are odd numbers")


# In[ ]:




