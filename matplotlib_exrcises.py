#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Within your codeup-data-science directory, create a new directory named numpy-pandas-visualization-exercises.

# This will be where you do your work for this module.
# Initialize this directory as a local repository, create a repository on GitHub with the same name,
# link the remote, and push your work.

# Do your work for this exercise in a jupyter notebook named matplotlib_exercises.

# 1. Use matplotlib to plot the following equation: "$y = x ** 2 − x + 2$"
# You'll need to write the code that generates the x and y points.
# Add an anotation for the point 0, 0, the origin.


# In[1]:


import matplotlib.pyplot as plt


# In[73]:


print(plt)


# In[36]:


x = list(range(100))
y = [(n ** 2 - n + 2) for n in x]
plt.plot(x, y)
plt.annotate('Origin', xy=(0, 0), xytext=(-4, 250))


# In[37]:


import math


# In[54]:


# 2. Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
# y=√x, y=x**3, y=2**x, y=1/(x+1) 
# You can use functions from the math module to help implement some of the equations above

plt.figure(figsize=(20,12))

plt.subplot(2,2,1)
x = list(range(100))
y = [math.sqrt(n) for n in x]
plt.plot(x,y)

plt.subplot(2,2,2)
x = list(range(100))
y = [n**3 for n in x]
plt.plot(x,y)

plt.subplot(2,2,3)
y = [2**n for n in x]
plt.plot(x,y)

plt.subplot(2,2,4)
y = [(1 / (n + 1)) for n in x]
plt.plot(x,y)


# In[63]:


# 3. Combine the figures you created in the last step into one large figure with 4 subplots.

plt.figure(figsize=(10,6))


x = list(range(5))
y = [math.sqrt(n) for n in x]
z = [n**3 for n in x]
a = [2**n for n in x]
b = [(1 / (n + 1)) for n in x]

plt.plot(x, y, c = "blue")
plt.plot(x, z, c = "orange")
plt.plot(x, a, c = "green")
plt.plot(x, b, c = "purple")


# In[77]:


# 4. Combine the figures you created in the last step into one figure
# where each of the 4 equations has a different color for the points.
# Be sure to include a legend and an appropriate title for the figure.
# y=√x, y=x**3, y=2**x, y=1/(x+1) 

plt.figure(figsize=(20,12))


x = list(range(5))
y = [math.sqrt(n) for n in x]
z = [n**3 for n in x]
a = [2**n for n in x]
b = [(1 / (n + 1)) for n in x]

plt.plot(x, y, c = "blue", label = "$=√x$")
plt.scatter(x, y, c = "blue")
plt.plot(x, z, c = "orange", label = "$y=x**3$")
plt.scatter(x, z, c = "orange")
plt.plot(x, a, c = "green", label = "$y=2**x$")
plt.scatter(x, a, c = "green")
plt.plot(x, b, c = "purple", label = "$y=1/(x+1)$")
plt.scatter(x, b, c = "purple")

plt.legend()


# In[ ]:


# Make a new Jupyter notebook named big_o_notation.ipynb

# Title your chart "Big O Notation"
# Label your x axis "Elements"
# Label your y axis "Operations"
# Label your curves or make a legend for the curves
# Use LaTex notation where possible
# Curves to graph

