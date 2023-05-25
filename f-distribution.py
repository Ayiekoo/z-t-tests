#!/usr/bin/env python
# coding: utf-8

# In[1]:


### f-distribution
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f
x = np.linspace(0, 4.5, 1000)
data_1 = f(1, 1, 0)
data_2 = f(5, 8, 0)
data_3 = f(4, 4, 0)
data_4 = f(100, 200, 0)
plt.figure(figsize=(12, 6), dpi = 150)
plt.plot(x,data_1.pdf(x), label = '1,1')
plt.plot(x, data_2.pdf(x), label = '5,8')
plt.plot(x, data_3.pdf(x), label = '4,4')
plt.plot(x, data_4.pdf(x), label = '100,200')
plt.legend()


# In[2]:


##Null Hypothesis = Variances are equal
##Alternative Hypothesis are not equal


# In[3]:


import random
random.seed(20)


# In[4]:


x = np.array([random.gauss(100,15) for x in range(20)])
y = np.array([random.gauss(100,15) for x in range(20)])


# In[5]:


f_test_stat = np.var(x,ddof=1) / np.var(y,ddof = 1)


# In[6]:


dfn = x.size - 1
dfd = x.size - 1


# In[7]:


p_value = 1 - f.cdf(f_test_stat,dfn,dfd)


# In[8]:


p_value ### p-value is < 0.5
## we have to accept the null hypothesis


# In[9]:


x = np.array([random.gauss(100,15) for x in range(20)])
y = np.array([random.gauss(100,15) for x in range(20)])


# In[10]:


f_test_stat = np.var(x,ddof=1) / np.var(y,ddof = 1)
dfn = x.size - 1
dfd = x.size - 1
p_value = 1 - f.cdf(f_test_stat,dfn,dfd)
p_value


# In[ ]:


## p-value > 0.5
## we need to reject the null hypothesis

## means the variance is not equal

