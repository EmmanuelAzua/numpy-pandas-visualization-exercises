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


tables = pd.read_sql("SHOW TABLES", url).drop(columns=['multiple_lines', 'C'])
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


# In[17]:


fig, first = plt.subplots(figsize=(15, 15))
first = sns.scatterplot(data = customers, x = "tenure", y = "payment_type_id", hue = "churn")


# In[18]:


sns.relplot(data = customers, x = "tenure", y = "contract_type_id", hue = "churn")


# In[19]:


sns.violinplot(data = customers, x = "payment_type_id", y = "contract_type_id", hue = "churn")


# In[20]:


sns.pointplot(data = customers, x = "streaming_movies", y = "senior_citizen", hue = "churn")


# In[21]:


sns.relplot(data = customers, x = "tenure", y = "senior_citizen", hue = "churn")


# In[22]:


sns.lineplot(data = monthly_customers, x = "payment_type_id", y = "churn")


# In[23]:


yearly_customers = customers[customers["contract_type_id"] == 2]
yearly_customers


# In[24]:


two_year_customers = customers[customers["contract_type_id"] == 3]
two_year_customers


# In[25]:


sns.pairplot(data = monthly_customers)


# In[46]:


spreadsheet = pd.read_excel("Spreadsheets_Exercises_Solutions.xlsx", sheet_name = "mytable_customer_details_values", header = 1)
spreadsheet


# In[47]:


spreadsheet.info()


# In[49]:


pearsoncorr = spreadsheet.corr(method = 'pearson')
pearsoncorr


# In[53]:


plt.figure(figsize = (16,5))
sns.heatmap(pearsoncorr, 
            xticklabels = pearsoncorr.columns,
            yticklabels = pearsoncorr.columns,
            cmap = 'RdBu_r',
            annot = True,
            linewidth = 0.5,
           center = 0)


# In[55]:


sns.pairplot(data = spreadsheet)


# In[61]:


sns.relplot(data = spreadsheet, x = "tenure", y = "average_monthly_charges", hue = "churn")


# In[123]:


monthly_customers = spreadsheet[spreadsheet["contract_type"] == 0]
monthly_customers


# In[137]:


yearly_customers = spreadsheet[spreadsheet["contract_type"] == 1]
yearly_customers


# In[138]:


twoyear_customers = spreadsheet[spreadsheet["contract_type"] == 2]
twoyear_customers


# In[124]:


sns.pairplot(data = monthly_customers)


# In[125]:


sns.relplot(data = monthly_customers, x = "tenure", y = "average_monthly_charges", hue = "churn")


# In[126]:


sns.lineplot(data = monthly_customers, x = "payment_type", y = "average_monthly_charges", hue = "churn")


# In[127]:


sns.lineplot(data = monthly_customers, x = "is_senior_citizen", y = "average_monthly_charges", hue = "churn")


# In[128]:


pearsons4monthly = monthly_customers.corr(method = 'pearson')
pearsons4monthly


# In[129]:


plt.figure(figsize = (16,5))
sns.heatmap(pearsons4monthly, 
            xticklabels = pearsoncorr.columns,
            yticklabels = pearsoncorr.columns,
            cmap = 'RdBu_r',
            annot = True,
            linewidth = 0.5,
           center = 0)


# In[130]:


plt.figure(figsize = (25,10))
sns.swarmplot(data = monthly_customers, x = "tenure", y = "payment_type", hue = "churn", size = 10)


# In[131]:


plt.figure(figsize = (16,5))
sns.relplot(data = monthly_customers, x = "tenure", y = "payment_type", hue = "churn")


# In[132]:


sns.lineplot(data = monthly_customers, x = "payment_type", y = "tenure", hue = "churn")


# In[133]:


sns.relplot(data = monthly_customers, x = "has_phone", y = "tenure", hue = "churn")


# In[134]:


sns.relplot(data = monthly_customers, x = "has_internet", y = "tenure", hue = "churn")


# In[135]:


sns.relplot(data = monthly_customers, x = "has_phone_and_internet", y = "tenure", hue = "churn")


# In[141]:


sns.relplot(data = monthly_customers, x = "is_senior_citizen", y = "payment_type", hue = "churn")


# In[210]:


total_churners = spreadsheet.groupby(["has_churned"]).count().iloc[:,14].sort_values(ascending = True).head(1) #[spreadsheet['has_churned'] == True] #monthly_customers[monthly_customers["has_churned" == True]].value_counts()
total_churners


# In[213]:


churner_groups = spreadsheet.groupby(["contract_type", "has_churned"]).count().iloc[:,14].sort_values(ascending = True)
churner_groups

