### Exercises Part I
## Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.
## Use pandas to create a Series named fruits from the following list:

## ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

## Use Series attributes and methods to explore your fruits Series
## 1. Determine the number of elements in fruits.

import numpy as np
import pandas as pd

fruits_series = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruits_series
0                 kiwi
1                mango
2           strawberry
3            pineapple
4           gala apple
5     honeycrisp apple
6               tomato
7           watermelon
8             honeydew
9                 kiwi
10                kiwi
11                kiwi
12               mango
13           blueberry
14          blackberry
15          gooseberry
16              papaya
dtype: object

fruits_series.size
17

## 2. Output only the index from fruits

fruits_series.index
RangeIndex(start=0, stop=17, step=1)

## 3. Output only the values from fruits

fruits_series.values
array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
       'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
       'papaya'], dtype=object)

## 4. Confirm the data type of the values in fruits

fruits_series.dtypes
dtype('O')

## 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits

fruits_series[:5]
0          kiwi
1         mango
2    strawberry
3     pineapple
4    gala apple
dtype: object

fruits_series[-3:]
14    blackberry
15    gooseberry
16        papaya
dtype: object

fruits_series.sample(n=3, random_state=1)
3      pineapple
13     blueberry
7     watermelon
dtype: object


## 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.

fruits_series.describe()
count       17
unique      13
top       kiwi
freq         4
dtype: object

## 7. Run the code necessary to produce only the unique string values from fruits.

fruits_series.unique

array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
       'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)


## 8. Determine how many times each unique string value occurs in fruits.

fruits_series.value_counts()

kiwi                4
mango               2
pineapple           1
watermelon          1
strawberry          1
gooseberry          1
tomato              1
honeycrisp apple    1
papaya              1
blackberry          1
honeydew            1
blueberry           1
gala apple          1

## 9. Determine the string value that occurs most frequently in fruits.

## 10. Determine the string value that occurs least frequently in fruits.



### Explore more attributes and methods while you continue to work with the fruits Series.

## 1. Capitalize all the string values in fruits

fruits_series.str.capitalize()

0                 Kiwi
1                Mango
2           Strawberry
3            Pineapple
4           Gala apple
5     Honeycrisp apple
6               Tomato
7           Watermelon
8             Honeydew
9                 Kiwi
10                Kiwi
11                Kiwi
12               Mango
13           Blueberry
14          Blackberry
15          Gooseberry
16              Papaya
dtype: object

## 2. Count the letter "a" in all the string values (use string vectorization).

fruits_series.str.count("a")

0     0
1     1
2     1
3     1
4     3
5     1
6     1
7     1
8     0
9     0
10    0
11    0
12    1
13    0
14    1
15    0
16    3
dtype: int64

fruits_series[fruits_series.str.count("a")]

0         kiwi
1        mango
1        mango
1        mango
3    pineapple
1        mango
1        mango
1        mango
0         kiwi
0         kiwi
0         kiwi
0         kiwi
1        mango
0         kiwi
1        mango
0         kiwi
3    pineapple
dtype: object

len(fruits_series.str.count("a"))
17



## 3. Output the number of vowels in each and every string value

fruits_series['Vowels'] = fruits_series.str.lower().str.count(r'[aeiou]')

fruits_series["Vowels"]

0         2.0
1         2.0
2         2.0
3         4.0
4         4.0
5         5.0
6         3.0
7         4.0
8         3.0
9         2.0
10        2.0
11        2.0
12        2.0
13        3.0
14        2.0
15        4.0
16        3.0
Vowels    NaN
dtype: float64



## 4. Write the code to get the longest string value from fruits

fruits_series.max()
'watermelon'

## 5. Write the code to get the string values with 5 or more letters in the name

fruits_series[fruits_series.str.len() > 5]

2           strawberry
3            pineapple
4           gala apple
5     honeycrisp apple
6               tomato
7           watermelon
8             honeydew
13           blueberry
14          blackberry
15          gooseberry
16              papaya
dtype: object

## 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times

fruits_series[fruits_series.apply(lambda str: "o" in str)]

1                mango
5     honeycrisp apple
6               tomato
7           watermelon
8             honeydew
12               mango
15          gooseberry
dtype: object

## 7. Write the code to get only the string values containing the substring "berry".

fruits_series[fruits_series.apply(lambda str: "berry" in str)]

2     strawberry
13     blueberry
14    blackberry
15    gooseberry
dtype: object

## 8. Write the code to get only the string values containing the substring "apple".

fruits_series[fruits_series.apply(lambda str: "apple" in str)]

3           pineapple
4          gala apple
5    honeycrisp apple
dtype: object

## 9. Which string value contains the most vowels?

def countvowels(str):
    num_vowels = 0
    for char in str:
        if char in str in ["aeiouAEIOU"]:
            num_vowels += 1
        return str
        
            

fruits_series.nlargest()
