#!/usr/bin/env python
# coding: utf-8

# In[1]:


### z test

import random
random.seed(20)
from statsmodels.stats.weightstats import ztest as ztest


# In[4]:


a = [random.gauss(100,15) for x in range(40)]


# a = [random.gauss(100,15) for x in range(40]

# In[5]:


ztest(a,value = 100)


# In[6]:


a = [random.gauss(120,15) for x in range(40)]
ztest(a,value = 100,alternative = 'larger')


# In[8]:


a = [random.gauss(80,15) for x in range(40)]
ztest(a,value=100,alternative = 'smaller')


# In[9]:


a = [random.gauss(100,15) for x in range(40)]
b = [random.gauss(120,15) for x in range(40)]


# In[11]:


ztest(a,b,value = 0)


# In[12]:


a = [random.gauss(100,15) for x in range(40)]
b = [random.gauss(100,15) for x in range(40)]


# In[13]:


ztest(a,b,value = 0)


# In[ ]:




