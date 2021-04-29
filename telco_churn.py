#!/usr/bin/env python
# coding: utf-8

# Storytelling Project Specifications
# 
# Scenario:
# You’re working as a Data Scientist at a Telecommunications company and the VP of Operations comes to you and says, “We need to reduce customer attrition! Our customers are leaving us for competitors at way too high a rate. Our VP of Sales says removing the month-to-month plan is NOT an option. I already know those customers leave the most, so I want you to focus on only the customers on the Month-to-Month plan. What do you think is driving them to churn? What can we do to try to keep these customers from leaving?”
# 
# Business Goal:
# Reduce customer attrition, a.k.a. Churn, among the customers on the month-to-month plan. Why? Because keeping customers is cheaper than getting new customers. 
# 
# Project Goal:
# A 3 minute presentation that communicates what you found, what your recommendation is, and how you expect the recommended action(s) to decrease the attrition. Your presentation will include: 
# a chart that undeniably demonstrates the source of attrition that you focused on.
# a single recommendation, backed by data, that we would expect to reduce some of the attrition we are seeing.
# a chart that visualizes what you would expect to see, in terms of reduction in churn, if the recommendation is taken.

# In[1]:


import pandas as pd
import numpy as np
from pydataset import data
import seaborn as sns
import matplotlib.pyplot as plt
import pymysql


# In[2]:


from env import username, password, host
def get_db_url(username, password, host):
    url = f'mysql+pymysql://{username}:{password}@{host}/telco_churn'
    return url


# In[3]:


url = get_db_url(username, password, host)


# In[4]:


tables = pd.read_sql("SHOW TABLES", url)
tables


# In[5]:


contract_types_structure = pd.read_sql('''DESCRIBE contract_types''', url)
contract_types_structure


# In[6]:


customers_structure = pd.read_sql('''DESCRIBE customers''', url)
customers_structure


# In[7]:


internet_service_types_structure = pd.read_sql('''DESCRIBE internet_service_types''', url)
internet_service_types_structure


# In[8]:


payment_types_structure = pd.read_sql('''DESCRIBE payment_types''', url)
payment_types_structure


# In[9]:


contract_types = pd.read_sql('''contract_types''', url)
contract_types


# In[10]:


customers = pd.read_sql('''customers''', url)
customers.head()


# In[11]:


customers.info()


# In[12]:


internet_service_types = pd.read_sql('''internet_service_types''', url)
internet_service_types


# In[13]:


payment_types = pd.read_sql('''payment_types''', url)
payment_types


# In[14]:


monthly_customers = customers[customers["contract_type_id"] == 1]
monthly_customers


# In[15]:


pearsoncorr = customers.corr(method = 'pearson')
pearsoncorr


# In[16]:


sns.heatmap(pearsoncorr, 
            xticklabels = pearsoncorr.columns,
            yticklabels = pearsoncorr.columns,
            cmap = 'RdBu_r',
            annot = True,
            linewidth = 0.5)


# In[20]:


fig, first = plt.subplots(figsize=(15, 15))
first = sns.scatterplot(data = customers, x = "tenure", y = "payment_type_id", hue = "churn")


# In[24]:


sns.relplot(data = customers, x = "tenure", y = "contract_type_id", hue = "churn")


# In[19]:


sns.violinplot(data = customers, x = "payment_type_id", y = "contract_type_id", hue = "churn")


# In[30]:


sns.pointplot(data = customers, x = "streaming_movies", y = "senior_citizen", hue = "churn")


# In[31]:


sns.relplot(data = customers, x = "tenure", y = "senior_citizen", hue = "churn")


# In[33]:


sns.lineplot(data = monthly_customers, x = "payment_type_id", y = "churn")


# In[ ]:


yearly_customers = customers[customers["contract_type_id"] == 2]
yearly_customers


# In[ ]:


two_year_customers = customers[customers["contract_type_id"] == 3]
two_year_customers


# In[ ]:


sns.pairplot(data = monthly_customers)


# In[ ]:




