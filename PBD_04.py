#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Lecture 4")


# In[6]:


s="University of Central Punjab"
type(s)


# In[7]:


s


# In[8]:


print(s)


# In[9]:


s[0]


# In[11]:


s[0:10]


# In[12]:


name="Tahir Mahmood Wahla"
type(name)


# In[13]:


name


# In[14]:


print(name)


# In[15]:


name[0:5]


# In[16]:


s[-2]


# In[17]:


s[-1]


# In[18]:


s[-20]


# In[19]:


s[-24]


# In[20]:


s[-25]


# In[21]:


s[-28]


# In[22]:


s[-1:-5]
#- range never work like that n=but its work when we give s[-5:-1] or s[-5:]


# In[23]:


s[-5:-1]


# In[24]:


s[-5:]


# In[25]:


s[-5:-1:2]


# In[26]:


s[-15:-1:2]


# In[27]:


s[-15:-1:2]


# In[28]:


city="Lahore"


# In[30]:


ucp =s+city


# In[31]:


s="University of Central Punjab"
type(s)


# In[32]:


city="Lahore"


# In[35]:


ucp =s+"  "+city


# In[36]:


ucp


# In[37]:


ucp.lower()


# In[38]:


ucp.upper()


# In[39]:


ucp


# In[41]:


len(ucp)


# In[42]:


ucp.split(" ")


# In[45]:


ucpHistory="On 15 August 1996, The Punjab Group of Colleges petitioned Government of Punjab for the establishment of a university in the province. \Punjab Institute of Computer Science (PICS), Punjab College of Commerce (PCC), Punjab Law College (PLC) and Punjab College of Information Technology (PCIT) formed the core of the university at the time of establishment.Following a restructuring in 2004, the PCBA and PICS operate under the Faculty of Management Studies and Faculty of Information Technology of the University of Central Punjab respectively. The Punjab Colleges of Commerce and the Punjab Law College respectively function under the Faculties of Commerce and of Law of the University of Central Punjab. The Faculty of Engineering (FOE) was introduced in 2002."


# In[49]:


ucpHistory


# In[52]:


length=len(ucpHistory)
Count=0
for i in range(length):
   if ucpHistory[i]>='A' and ucpHistory[i]<='Z' or ucpHistory[i]>='a' and ucpHistory[i]<='z':
    Count=Count+1
    
print(Count)


# In[59]:


length=len(ucpHistory)
for i in range(length):
    if ucpHistory[i]=='o':
        if ucpHistory[i+1]=='f':
            ucpHistory[i]==" "
        

        
print(ucpHistory)

