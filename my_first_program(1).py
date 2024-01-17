#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


print("sonal")


# #### Data Types

# In[1]:


x=12
type(x)


# In[2]:


x=4.7
type(x)


# In[3]:


x="hello"
type(x)


# In[6]:


x=True
type(x)


# In[7]:


x="False"
type(x)


# In[8]:


x=False
type(x)


# ## variables

# In[10]:


names="a","b"
names


# In[11]:


2names="a","b"
2names


# In[12]:


n2ames="a","b"
n2ames


# ## variable name should not start with a numbers

# In[13]:


names-list="a","b","c"
names-list


# In[14]:


names_list="a","b","c"
names_list


# ### only allowed special symbol is underscore

# In[15]:


Name="Sonal"
Age=21
Income=100000


# In[16]:


print(Age)
print(Name)
print(Income)


# In[17]:


name list="sona","piyu"
name list


# ### Space Is Not allowed

# ## *List*

# In[23]:


sample_list=[1,2,3,4,"hii",-3,11,2,2,6.1]
sample_list


# In[24]:


type(sample_list)


# In[25]:


sample_list[0]


# In[26]:


sample_list[5]


# In[27]:


sample_list[4]


# In[28]:


sample_list[10]


# In[29]:


sample_list[-2]


# ### negative index always starts fron negative one from right side

# In[31]:


sample_list[0]=100
sample_list


# #### If we want to change the value from list

# ###Elements in a list are seperated by comma and enclosed in square brackets

# ###list is hetrogenous-> Multiple data types

# ###List can have duplicates

# ###List is mutable->make changes

# ## Tuple
# 
# #### contain object
# #### Heterogenous-> allows multiple data types
# #### Can have duplicates
# #### Immutable->cannot make changes
# #### In tuple elements are seperated by comma,enclosed in paranthesis or without any brackets
# 

# In[33]:


sample_tuple=(1,2,4,6,"hi",3.1)
sample_tuple


# In[34]:


type(sample_tuple)


# In[35]:


sample_tuple2=1,2,4,6,"hi",3.1
sample_tuple2


# In[36]:


sample_tuple[2]


# In[37]:


sample_tuple[10]


# In[38]:


sample_tuple[0]=120


# ## Dictionary

# ### 1) Key-value pair
# ### 2) { }
# ### 3) Indexing-square brackets
# ### 4) Mutable

# In[39]:


dict={'Name':"Sonal","Hobbies":["cooking","dancing","painting"],1:23}
dict


# In[40]:


dict[keys]


# In[41]:


dict.keys()


# In[42]:


dict.values()


# In[44]:


dict['Name']="Snehal"
dict


# In[45]:


del dict['Name']
dict


# In[46]:


### Add a new key values
dict.update({"class":"TE"})
dict


# In[47]:


len(dict)


# In[48]:


type(dict)


# In[49]:


dict.items()


# In[51]:


dict.get("Hobbies")


# In[52]:


dict.get("class")


# ## Sets

# In[53]:


set={1,2,3,6,4,5,6,1,"hi","TE",-2,2.4,6,9,54,1.0}
set


# In[54]:


set[0]
set


# In[55]:


set[0]=9
set


# In[56]:


set.add(100)
set


# In[57]:


set.remove(5)
set


# ### Set does not allow duplicates
# ### we cannot retrive the set using index
# ### Set is mutable
# ### Set has {}
# ### Ordered-First place

# In[ ]:




