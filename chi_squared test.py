#!/usr/bin/env python
# coding: utf-8

# In[1]:


### chi-squared distribution and test
import numpy as np


# In[2]:


data1 = np.random.chisquare(df = 1,size = 1000)
data2 = np.random.chisquare(df = 2,size = 1000)
data3 = np.random.chisquare(df = 3,size = 1000)


# In[3]:


print(data1[:10])


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


sns.distplot(data1,hist = False,label = 'dof 1')
sns.distplot(data2,hist = False,label = 'dof 2')
sns.distplot(data3,hist = False,label = 'dof 3')
plt.legend()


# In[16]:


from scipy.stats import chi2_contingency


# In[17]:


### chi-square test 

## checks relationships between the datasets


data = [[10,20,30],[6,9,17]]


# In[20]:


stat,p_value,dof,chi_array = chi2_contingency(data)


# In[21]:


p_value  ### a p-value >0.5 is generated
### we reject the hypothesis


# In[22]:


### let's modify the data

data = [[10,20,30],[9,1,8]]


# In[23]:


stat,p_value,dof,chi_array = chi2_contingency(data)


# In[24]:


p_value ### p-value less than 0.5 obtained; accept the hypothesis
## no association between the groups


# In[ ]:


### chi-squared test and goodness of fit

