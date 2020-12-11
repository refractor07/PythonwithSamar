#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
print('All set')


# In[6]:


#importing libraries

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[66]:


#importing datasets

athlete_data = pd.read_csv ('F:\\MTECH\\DATASCI\\athletes.csv')
country_data = pd.read_csv ('F:\\MTECH\\DATASCI\\countries.csv')
bp=pd.read_csv ('F:\\MTECH\\DATASCI\\bp.csv')
#bp=pd.read_csv ('F:\\MTECH\\DATASCI\\bp.xlsx')


tips_data = sns.load_dataset('tips')


# In[41]:


athlete_data.head(10)


# In[19]:


country_data.head(10)


# In[20]:


tips_data.head(10)


# In[24]:


sns.relplot(x= 'height',y='weight',data=athlete_data)
plt.show( )


# In[25]:


sns.relplot(x= 'height',y='weight',hue='sex',data=athlete_data)
plt.show( )


# In[26]:


sns.relplot(x= 'height',y='weight',hue='sport',data=athlete_data)
plt.show( )


# In[27]:


sns.catplot(x='day',y='tip',data=tips_data)


# In[29]:


sns.catplot(x='day',y='tip',kind='swarm',data=tips_data)


# In[30]:


sns.catplot(x='day',y='tip',hue='sex',kind='swarm',data=tips_data)


# In[31]:


sns.catplot(x='day',y='tip',hue='sex',kind='box',data=tips_data)


# In[33]:


sns.catplot(x='day',y='tip',hue='sex',kind='violin',data=tips_data)


# In[39]:


sns.countplot(x=athlete_data("sport"),order = athlete_data("sport").value_counts().index)
plt.show( )


# In[42]:


sns.distplot(tips_data['total_bill'],kde= False)


# In[43]:


sns.distplot(tips_data['total_bill'],kde= True)


# In[45]:


sns.jointplot(x=tips_data['total_bill'],y=tips_data['tip'],kind='kde')


# In[48]:


sns.relplot(x= 'height',y='weight',hue='sport',height=7,aspect=2,data=athlete_data)
plt.show( )


# In[73]:


bp.head(25)


# In[75]:


sns.relplot(x= 'DAY1',y='NIGHT1',data=bp)
plt.show( )


# In[ ]:




