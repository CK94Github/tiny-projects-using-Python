#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
print(pd.__version__)


# # DataFrame creation

# ## Create an empty pandas DataFrame

# In[2]:


pd.DataFrame(data=[None],
            index=[None],
            columns=[None])


# ##  Create a marvel_df pandas DataFrame with the given marvel data

# In[3]:


marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]


# In[4]:


marvel_df = pd.DataFrame(data=marvel_data)
marvel_df


# ## Add column names to the marvel_df

# In[5]:


col_names = ['name', 'sex','first_appearance']

marvel_df.columns =col_names
marvel_df


# ## Add index names to the marvel_df (use the character name as index)

# In[6]:


marvel_df.index = marvel_df['name']
marvel_df


# ### Drop the name column as it's now the index

# In[7]:


marvel_df=marvel_df.drop(['name'], axis=1)
marvel_df


# ### Drop 'Namor' and 'Hank Pym' rows

# In[11]:


marvel_df = marvel_df.drop(['Namor','Hank Pym'],axis=0)
marvel_df


# In[ ]:




