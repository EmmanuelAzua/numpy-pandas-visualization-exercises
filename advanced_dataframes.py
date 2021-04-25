#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pydataset import data


# In[2]:


from env import username, password, host
def get_db_url(username, password, host):
    url = f'mysql+pymysql://{username}:{password}@{host}/employees'
    return url


# In[3]:


url = get_db_url(username, password, host)


# In[4]:


pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)


# In[5]:


sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''

employees = pd.read_sql(sql, url)
employees.head()


# In[6]:


query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()


# '''
# Exercises I
# 
# Run python -m pip install mysqlclient pymysql from your terminal to install pymysql and the mysqlclient.
# 
# Create a notebook or python script named advanced_dataframes to do your work in for these exercises.
# 
# 1. Create a function named get_db_url. It should accept a username, hostname, password, and database name
# and return a url connection string formatted like in the example at the start of this lesson.
# 
# 2. Use your function to obtain a connection to the employees database.
# 
# 3. Once you have successfully run a query:
# 
#     a. Intentionally make a typo in the database url. What kind of error message do you see?
# 
#     b. Intentionally make an error in your SQL query. What does the error message look like?
# 
# 4. Read the employees and titles tables into two separate DataFrames.
# 
# 5. How many rows and columns do you have in each DataFrame? Is that what you expected?
# 
# 6. Display the summary statistics for each DataFrame.
# 
# 7. How many unique titles are in the titles DataFrame?
# 
# 8. What is the oldest date in the to_date column?
# 
# 9. What is the most recent date in the to_date column?'''

# In[5]:


employees = '''
SELECT *
FROM employees
'''

test_query = pd.read_sql(employees, url)
test_query.head()


# In[106]:


# a. Intentionally make a typo in the database url. What kind of error message do you see?
# R. AttributeError: module 'pandas' has no attribute 'read_sq'

employees = '''
SELECT *
FROM employees
'''

test_query = pd.read_sql(employees, url)
test_query.head()


# In[107]:


# b. Intentionally make an error in your SQL query. What does the error message look like?
# R. ProgrammingError: (pymysql.err.ProgrammingError) (1146, "Table 'employees.employes' doesn't exist")
# [SQL: 
# SELECT *
# FROM employes
# ]
# (Background on this error at: http://sqlalche.me/e/13/f405)


employees = '''
SELECT *
FROM employees
'''

test_query = pd.read_sql(employees, url)
test_query.head()


# In[17]:


# 4.- Read the employees and titles tables into two separate DataFrames.

first_table = pd.read_sql('''DESCRIBE employees''', url)
first_table


# In[108]:


second_table = pd.read_sql('''DESCRIBE titles''', url)
second_table


# In[109]:


joint_tables = pd.read_sql('''SELECT *
                            FROM employees
                            JOIN titles ON titles.emp_no = employees.emp_no''', url)
joint_tables


# In[110]:


df1 = joint_tables.iloc[:, :6]
df1


# In[111]:


df2 = joint_tables.iloc[:, 6:]
df2


# In[112]:


# 5. How many rows and columns do you have in each DataFrame? Is that what you expected?
joint_tables = pd.read_sql('''SELECT *
                            FROM employees
                            JOIN titles ON titles.emp_no = employees.emp_no''', url)
df1 = pd.DataFrame(joint_tables.iloc[:, :6])
df2 = pd.DataFrame(joint_tables.iloc[:, 6:])
display(df1), display(df2)


# In[50]:


#  6. Display the summary statistics for each DataFrame

df1.describe(), df2.describe()


# In[52]:


# 7. How many unique titles are in the titles DataFrame?
df2.nunique()


# In[68]:


# 8. What is the oldest date in the to_date column?

df2.sort_values(by = "to_date").head(1).iloc[:, 3:]


# In[140]:


# 9. What is the most recent date in the to_date column?''

import datetime
# df2[(df2['to_date'] < datetime.date(9999,1,1))]

df2[(df2['to_date'] < datetime.date(9999,1,1))].sort_values(by = "to_date", ascending = False).head(1).iloc[:, 3:]


# In[9]:


# Exercises II
# 1. Copy the users and roles DataFrames from the examples above


# In[4]:


# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[38]:


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# In[14]:


# 2. What is the result of using a right join on the DataFrames?
# R.- how = right: use only keys from right frame, similar to a SQL right outer join; preserve key order.

pd.merge(users, roles, how = "right")


# In[15]:


# 3. What is the result of using an outer join on the DataFrames?
pd.merge(users, roles, how = "outer")


# In[16]:


# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?

pd.merge(users, roles, how = "outer").drop(columns = "role_id")


# In[6]:


# 5. Load the mpg dataset from PyDataset

from pydataset import data
data("mpg")


# In[7]:


# 6. Output and read the documentation for the mpg dataset

data("mpg", show_doc = True)


# In[8]:


# 7. How many rows and columns are in the dataset?
# R. 234 rows, and 11 columns/variables


# In[9]:


# 8. Check out your column names and perform any cleanup you may want on them
mpg = data("mpg")


# In[10]:


# 9. Display the summary statistics for the dataset

mpg.describe()


# In[11]:


# 10.1. How many different manufacturers are there?
# Can answer this question in different formats
# We can manually count the number of rows/names

mpg.groupby("manufacturer").count() #1
mpg.groupby("manufacturer").count().drop(columns = ["model", "displ", "year", "cyl", "trans", "drv", "cty", "hwy", "fl", "class"]) #2, cleaner


# In[12]:


# 10.2. How many different manufacturers are there?
# Alternatively:

number_of_manufacturers = len(mpg.groupby("manufacturer").count())
print("Total Number of Manufacturers in Dataframe is: ", number_of_manufacturers)


# In[13]:


# 11.1. How many different models are there?
# Can answer this question in different formats as well
# Counting the number of rows manually

mpg.groupby("model").count() #1
mpg.groupby("model").count().drop(columns = ["manufacturer", "displ", "year", "cyl", "trans", "drv", "cty", "hwy", "fl", "class"]) #2, cleaner


# In[14]:


# 11.2. How many different models are there?
# We can also clean this up by:

models_variety = len(mpg.groupby("model").count())
print("The total number of models, regardless of manufacturer is: ", models_variety)


# In[16]:


# 12. Create a column named mileage_difference like you did in the DataFrames exercises;
# this column should contain the difference between highway and city mileage for each car.

mpg["mileage_difference"] = (mpg["hwy"] - mpg["cty"])
mpg


# In[30]:


# 13. Create a column named average_mileage like you did in the DataFrames exercises;
# this is the mean of the city and highway mileage.

mpg["average_mileage"] = (mpg["hwy"] + mpg["cty"]) / 2
mpg


# In[29]:


# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting
# whether the car has an automatic transmission.

mpg["is_automatic"] = np.where(mpg["trans"].str.contains("auto"), True, False)
mpg


# In[82]:


# Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?

# mpg.#.groupby("manufacturer")#.count()##.head(1).iloc(:, )
mpg.sort_values(by = "average_mileage", ascending = False).groupby("manufacturer").agg("mean").head(1)


# In[30]:


# Do automatic or manual cars have better miles per gallon

mpg.sort_values(["average_mileage", "is_automatic"], ascending = False).head(3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


# For each title, find the hire date of the employee that was hired most recently with that title.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




