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


# In[26]:


spreadsheet = pd.read_excel("Spreadsheets_Exercises_Solutions.xlsx", sheet_name = "mytable_customer_details_values", header = 1)
spreadsheet


# In[27]:


spreadsheet.info()


# In[28]:


pearsoncorr = spreadsheet.corr(method = 'pearson')
pearsoncorr


# In[29]:


plt.figure(figsize = (16,5))
sns.heatmap(pearsoncorr, 
            xticklabels = pearsoncorr.columns,
            yticklabels = pearsoncorr.columns,
            cmap = 'RdBu_r',
            annot = True,
            linewidth = 0.5,
           center = 0)


# In[30]:


sns.pairplot(data = spreadsheet)


# In[31]:


sns.relplot(data = spreadsheet, x = "tenure", y = "average_monthly_charges", hue = "churn")


# In[32]:


monthly_customers = spreadsheet[spreadsheet["contract_type"] == 0]
monthly_customers


# In[33]:


yearly_customers = spreadsheet[spreadsheet["contract_type"] == 1]
yearly_customers


# In[34]:


twoyear_customers = spreadsheet[spreadsheet["contract_type"] == 2]
twoyear_customers


# In[35]:


sns.pairplot(data = monthly_customers)


# In[36]:


sns.relplot(data = monthly_customers, x = "tenure", y = "average_monthly_charges", hue = "churn")


# In[37]:


sns.lineplot(data = monthly_customers, x = "payment_type", y = "average_monthly_charges", hue = "churn")


# In[38]:


sns.lineplot(data = monthly_customers, x = "is_senior_citizen", y = "average_monthly_charges", hue = "churn")


# In[39]:


pearsons4monthly = monthly_customers.corr(method = 'pearson')
pearsons4monthly


# In[40]:


plt.figure(figsize = (16,5))
sns.heatmap(pearsons4monthly, 
            xticklabels = pearsoncorr.columns,
            yticklabels = pearsoncorr.columns,
            cmap = 'RdBu_r',
            annot = True,
            linewidth = 0.5,
           center = 0)


# In[41]:


plt.figure(figsize = (25,10))
sns.swarmplot(data = monthly_customers, x = "tenure", y = "payment_type", hue = "churn", size = 10)


# In[42]:


plt.figure(figsize = (16,5))
sns.relplot(data = monthly_customers, x = "tenure", y = "payment_type", hue = "churn")


# In[43]:


sns.lineplot(data = monthly_customers, x = "payment_type", y = "tenure", hue = "churn")


# In[44]:


sns.relplot(data = monthly_customers, x = "has_phone", y = "tenure", hue = "churn")


# In[45]:


sns.relplot(data = monthly_customers, x = "has_internet", y = "tenure", hue = "churn")


# In[46]:


sns.relplot(data = monthly_customers, x = "has_phone_and_internet", y = "tenure", hue = "churn")


# In[47]:


sns.relplot(data = monthly_customers, x = "is_senior_citizen", y = "payment_type", hue = "churn")


# In[48]:


total_churners = spreadsheet.groupby(["contract_type_desc"])[["has_churned"]].count()#.iloc[:,14].sort_values(ascending = True).head(1) #[spreadsheet['has_churned'] == True] #monthly_customers[monthly_customers["has_churned" == True]].value_counts()
total_churners


# In[49]:


churner_groups = spreadsheet.groupby(["contract_type_desc", "has_churned"]).count().iloc[:,14].sort_values(ascending = False)
churner_groups


# In[50]:


total_churners = spreadsheet.groupby("contract_type_desc")[['has_churned']].sum().sort_values(by = "has_churned", ascending = False)
total_churners


# In[51]:


monthly_churners = spreadsheet.groupby("contract_type_desc")[['has_churned']].sum().sort_values(by = "contract_type_desc", ascending = False).head(1)
monthly_churners


# In[52]:


annual_churners = spreadsheet.groupby("contract_type_desc")[['has_churned']].sum().sort_values(by = "contract_type_desc", ascending = True).head(1)
annual_churners


# In[53]:


biannual_churners = spreadsheet.groupby("contract_type_desc")[['has_churned']].sum().sort_values(by = "has_churned").head(1)
biannual_churners
#biannual_churners2 = biannual_churners[biannual_churners["contract_type_desc"] == "2 Year"]


# In[54]:


plt.xticks(rotation=45)
total_churners_plot = sns.lineplot(data = total_churners)


# In[55]:


spreadsheet = pd.read_excel("Spreadsheets_Exercises_Solutions.xlsx", sheet_name = "mytable_customer_details_values", header = 1)
spreadsheet


# In[69]:


spreadsheet.info()


# In[110]:


spreadsheet_monthly = spreadsheet[spreadsheet["contract_type_desc"] == "Month-to-Month"]
monthly_useful_variables = spreadsheet_monthly[["contract_type_desc", "has_churned", "is_senior_citizen", "payment_type", "average_monthly_charges", "has_internet", "has_phone", "partner", "dependents"]]
monthly_useful_variables = monthly_useful_variables.replace({"partner": {"Yes": True, "No": False}})
monthly_useful_variables = monthly_useful_variables.replace({"dependents": {"Yes": True, "No": False}})
monthly_useful_variables


# In[112]:


pearsons_monthly = monthly_useful_variables.corr(method = 'pearson')
pearsons_monthly


# In[127]:


plt.figure(figsize = (16,5))
sns.heatmap(pearsons_monthly, 
            xticklabels = pearsons_monthly.columns,
            yticklabels = pearsons_monthly.columns,
            cmap = 'RdBu_r',
            annot = True,
            linewidth = 0.5,
           center = 0)


# In[136]:


avg_charges_m2m = (monthly_useful_variables["average_monthly_charges"].sum() / len(monthly_useful_variables["average_monthly_charges"]))
avg_charges_m2m

