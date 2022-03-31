#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Lecture 3
'''for(int x=0;x<1;x++){
    cout<<x<<endl;
    
}'''

for x in range(10):
    print(x)


# In[ ]:


for x in range(2,10,2):
    print(x)


# In[ ]:


for x in range(2,10,3):
    print(x)


# In[ ]:


x=10
i=50
for x in range(i,x-2,2):
    print(x)


# In[ ]:


x=10
i=50
for x in range(i,x,-2):
    print(x)


# In[ ]:


x=10
i=50
for x in range(i,x,-2):
    print(x,end=" ")


# In[ ]:


x=int(input("Enter the value of X:\n"))
for i in range(x):
    if i % 3 ==0:
        print(i,end=" ")


# In[ ]:


x=int(input("Enter the value of X:\n"))
for i in range(x):
    if i % 3 ==0:
        print(i,end=" ")
        
        


# In[ ]:


x=111
while x<999:
    y=x%10
    if y%2==0:
        print(x)
        
    x=x//10


# In[5]:


for x in range(111,999,1):
    a=x
    Count=0
    while a!=0:
        if a%2!=0:
            Count+=1
        a//=10
    if Count==3:
        print(x,end=" ")
   


# In[ ]:




