#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 
a=123, #get type and isinstance
b="123" # get type and isinstance
c=123.0 # get type and is instance


# In[2]:


a=123
print(type(a))
print(isinstance(a,int))


# In[3]:


b="123"
print(type(b))
print(isinstance(b,str))


# In[4]:


c=123.0
print(type(c))
print(isinstance(c,float))


# In[5]:


e=int(b)
print(type(e))


# In[6]:


a="demo"
b=int(a)    # because in string we can only transfered no not character


# In[7]:


### 
name="arun"
age=12
location="mumbai"

name1="kumar"
age1=25
location1="delhi"

a=["arun","12","mumbai"]
#type, isinstance,len,min,max,sorted


# In[8]:


a=["arun","12","mumbai"]
print(type(a))


# In[9]:


print(isinstance(a,list))


# In[10]:


print(len(a))


# In[11]:


print(min(a))


# In[14]:


print(max(a))


# In[15]:


print(min(a))


# In[16]:


print(sorted(a))


# In[17]:


print(a[0])


# In[18]:


print(a[-1])


# In[21]:


print(a[::-1])


# In[22]:


a=[1,2,3,4,"hello"]
a.append(10)


# In[23]:


print(a)


# In[24]:


a.insert(2,"hello")


# In[25]:


print(a)


# In[27]:


a.remove("hello")


# In[28]:


print(a)


# In[29]:


del a[0]


# In[30]:


print(a)


# In[31]:


a.insert(0,"hello")


# In[32]:


print(a)


# In[33]:


b=a.pop()
print(a)
print(b)


# In[34]:


print(a)
b=a.pop(3)
print(a)
print(b)


# In[ ]:


#Assiangement
a=["arun","kumar","kishore"]
#get first list first word -a
#get first list last word -n
#get last list first word-k
#get last list last word -e

# also get list as input from user & check the data types.

