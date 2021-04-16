### In your numpy-pandas-visualization-exercises repo, create a file named numpy_exercises.py for this exercise.

## Use the following code for the questions below:
## a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
# R.- 4  |  array([-2, -1, -6, -7])  |  a < 0     array([False, False, False, False,  True,  True, False, False, False, True, False,  True])

import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a[a < 0]


# 2. How many positive numbers are there?
# R.- 5  |  array([ 4, 10, 12, 23,  3]

a[a > 0]

# 3. How many even positive numbers are there?
# R.- 3  |   array([ 4, 10, 12])

a[a > 0 ]
array([ 4, 10, 12, 23,  3])

b = a[a > 0]
b[b % 2 == 0]
array([ 4, 10, 12])

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
# R.- 10  | array([ 7, 13, 15, 26,  1,  2,  3,  3,  3,  6])

a + 3
c = a + 3
c
array([ 7, 13, 15, 26,  1,  2,  3,  3,  3, -3,  6, -4])

c[c > 0]
array([ 7, 13, 15, 26,  1,  2,  3,  3,  3,  6])

len(c[c > 0])
10

# 5. If you squared each number, what would the new mean and standard deviation be?
# R.- 144.0243035046516 and 74.0

np.square(a)
array([ 16, 100, 144, 529,   4,   1,   0,   0,   0,  36,   9,  49])

d = np.square(a)
d
array([ 16, 100, 144, 529,   4,   1,   0,   0,   0,  36,   9,  49])

d.std()
144.0243035046516

d.mean()
74.0

# 6. A common statistical operation on a dataset is centering.
# This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point.
# Center the data set. See this link for more on centering.
# R.-

d - 74
array([-58,  26,  70, 455, -70, -73, -74, -74, -74, -38, -65, -25])

e = d - 74
e
array([-58,  26,  70, 455, -70, -73, -74, -74, -74, -38, -65, -25])

e.mean()
0.0

# 7. Calculate the z-score for each data point. Recall that the z-score is given by: z = (x - M) / o

z = (d - d.mean()) / d.std()
z
array([-0.40270981,  0.18052509,  0.48602908,  3.15918903, -0.48602908,
       -0.5068589 , -0.51380217, -0.51380217, -0.51380217, -0.26384436,
       -0.45131272, -0.17358181])

# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
sum_of_a
55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_af_a = min(a)
min_of_a
1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
max_of_a
10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a) / len(a)
mean_of_a
5.5

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = numpy.prod(a)
product_of_a
3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = [(n * n) for n in a]
squares_of_a
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
odds_in_a = a[a % 2 != 0]
odds_in_a
array([1, 3, 5, 7, 9])

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = a[a % 2 == 0]
evens_in_a
array([ 2,  4,  6,  8, 10])

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array([3,4,5,6,7,8])
b = np.arange(3,9).reshape(2,3)
b
array([[3, 4, 5],
       [6, 7, 8]])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.

# Exercise 10 - transpose the array b.

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2




