#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst=[1,2,3,4,5]


# In[2]:


list


# In[3]:


lst


# In[4]:


type(lst)


# In[5]:


lst=lst+[3.14,213.125,2.45]


# In[6]:


lst


# In[7]:


len(lst)


# In[8]:


lst=lst+["UCP","Lahore"]
lst


# In[10]:


lst[0:5]


# In[12]:


print(lst[0:5])
lst[0:5:2]


# In[13]:


#lst.clear()
lst


# In[14]:


lst.extend([9,8,7,6,5,4])
lst


# In[16]:


#append add the sublist at the end of exiting list
lst.append(['umt','pucit','ucp'])
lst


# In[17]:


#the resron opf this is is treated the the sublist as a index
lst[-1]


# In[19]:


lst[7:]


# In[21]:


len(lst)


# In[23]:


lst[16]


# In[25]:


lst[16][2]


# In[26]:


type(lst[16][1])


# In[27]:


lst.insert(0,100)
lst


# In[28]:


#del
#remove
#pop
lst.pop()


# In[29]:


lst


# In[35]:


len(lst)


# In[37]:


del lst[15]


# In[38]:


lst


# In[40]:


lst.remove('Lahore')


# In[42]:


lst


# In[43]:


lst.remove('UCP')


# In[44]:


lst


# In[45]:


lst.remove(2)


# In[46]:


lst


# In[47]:


type(lst)


# In[48]:


lst.sort()


# In[49]:


lst


# In[50]:


lst.sort(reverse=True)
lst


# In[51]:


#Dictionary.......
#Key :Single: Value(s) or Multiple Value its cvannot be duplicate its always unique
d={'Country':['Pakistan','India','Iran','China','Afghanistan'],
  'Capital':['Islamabad','New Dehli','Tehran','Beijing','Kabul'],
   'Population':[24.5,135.7,22.4,178.1,5.8]}


# In[52]:


d


# In[53]:


d.items()


# In[54]:


d.values()


# In[57]:


d.keys()


# In[58]:


for k,v in d.items():
    print(k," => ",v)


# In[60]:


for k in d.keys():
    print(k)


# In[61]:


for k,v in d.items():
    print(k," == ",type(k)," => ",v,type(v))


# In[62]:


t=(1,2,3,'ucp',5)
t


# In[64]:


type(t)


# In[66]:


t[3]


# In[67]:


t[2:5]


# In[68]:


#Error Becuase Tuple is constent and not changeable
t[1]=155


# In[69]:


t=(1,2,3,'ucp',5)+t
t


# #pandas

# #UHFJ

# In[70]:


import pandas as pd


# In[ ]:




