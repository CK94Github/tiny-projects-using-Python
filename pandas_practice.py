#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


a=[1,2,3,4,5,10]


# In[3]:


pd.Series(a)


# In[4]:


print(a[0])


# In[5]:


pd.Series(a, index=['a','b','c','d','e','f'])

WAP to convert given a dictionary into corresponding dataframe and display it.

dictionary = {'name': ['Vinay', 'Kushal', 'Aman'],

          	            'age' : [22, 25, 24],

          	            'occ' : ['engineer', 'doctor', 'accountant']}
# In[6]:


dictionary = {'name': ['Vinay', 'Kushal', 'Aman'],

          	            'age' : [22, 25, 24],

          	            'occ' : ['engineer', 'doctor', 'accountant']}


# In[7]:


dictionary


# In[8]:


pd.Series(dictionary)


# # Reading external data and plotting
# 
# 

# In[9]:


df= pd.read_csv('practice_small.csv')
df


# In[10]:


df.head()


# In[11]:


df.isna().sum()


# In[12]:


newdf= df.fillna(0)
newdf

#here we can fill all missing values with zero.


# In[13]:


new_df= df.fillna(method="ffill")
new_df


# In[14]:


newdf= df.fillna({
    'CodingActivities':0,
    'RemoteWork': 'not avalaible',
    'Employment':0,
    'TrueFalse_2':0,
    'TrueFalse_3':0,
    'SurveyLength':0,
    'SurveyEase':0,
    'ConvertedCompYearly':0,
    'EdLevel':0,
    'LearnCode':0,
    'LearnCodeOnline':0
})
newdf

#if we want to customized the missing values, we can use one dictionery to fill missing values of specific columns


# In[15]:


#newdf= df.fillna(method="ffill")
#newdf 
#ffill will carry forword previous values


# In[18]:


newdf= df.fillna(method="bfill", axis=0)
newdf

#backfill / bfill: use next valid observation to fill gap
#axis{0 or ‘index’, 1 or ‘columns’} Axis along which to fill missing values. For Series this parameter is unused and defaults to 0.

# axis = 0 for index and axis=1 for columns


# In[ ]:





# In[ ]:




