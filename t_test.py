#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### T test & p-value
"""
USES OF T-TEST
>> when determining if means of 2 groups are different or not
>> when we want to compare 2 samples
>> sample size <= 30
data flows normal distribution
"""


# In[2]:


import random


# In[4]:


a = [ random.gauss(50,20) for x in range(30)]
b = [ random.gauss(55,15) for x in range(30)]


# In[5]:


import seaborn as sns
sns.set_style('darkgrid')
sns.kdeplot(a,shade = True)
sns.kdeplot(b,shade = True)


# In[6]:


### independent sample t-test on the data
import scipy.stats as stats


# In[7]:


t_stat,p_value = stats.ttest_ind(a,b,equal_var=False)


# In[8]:


t_stat,p_value


# In[9]:


import numpy as np


# In[10]:


np.mean(a), np.mean(b)


# In[11]:


a = [ random.gauss(50,20) for x in range(30)]
b = [ random.gauss(60,25) for x in range(30)]


# In[20]:


t_stat,p_value = stats.ttest_ind(a,b,equal_var=False)


# In[21]:


t_stat,p_value


# In[13]:





# In[14]:





# In[18]:


np.mean(b) - np.mean(a)


# In[22]:


t_stat,p_value = stats.ttest_1samp(a,40,axis = 0)


# In[23]:


t_stat,p_value


# In[ ]:




