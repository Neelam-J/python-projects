#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = '2019'
url_link = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

#combining the url strings + year string together
url = url_link.format(year)
url


# ### return list of url given a list of years

# In[4]:


years = [2015,2016,2017,2018,2019]
url_link = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

for year in years:
    url = url_link.format(year)
    print(url)


# ## Read html webpage into pandas

# In[5]:


import pandas as pd


# In[6]:


df = pd.read_html(url, header=0)
df


# In[7]:


len(df)


# In[8]:


#Selecting the table

df[0]


# In[9]:


df2019=df[0]


# ## Data Cleaning
# 
# ### table header is presented multiple multiple times in several rows

# In[10]:


df2019[df2019.Age == 'Age']


# In[11]:


len(df2019[df2019.Age == 'Age'])


# In[12]:


df = df2019.drop(df2019[df2019.Age == 'Age'].index)


# In[13]:


df.shape


# ## EDA

# In[27]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[17]:


sns.displot(df.PTS, 
             kde = False)


# In[39]:


sns.displot(df.PTS, kde=False, color='blue', edgecolor="black", linewidth=0.5)
plt.show()
sns.histplot(df.PTS, kde=False, color='blue', edgecolor="black", linewidth=0.5)
plt.show()


# In[ ]:




