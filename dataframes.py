{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python385jvsc74a57bd0e134e05457d34029b6460cd73bbf1ed73f339b5b6d98c95be70b69eba114fe95",
   "display_name": "Python 3.8.5 64-bit ('base': conda)"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercises\n",
    "# Do your work for this exercise in a python script or a jupyter notebook with the name dataframes.py or dataframes.ipynb.\n",
    "\n",
    "# For several of the following exercises, you'll need to load several datasets using the pydataset library. (If you get an error when trying to run the import below, use pip to install the pydataset package.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pydataset import data\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# When the instructions say to load a dataset, you can pass the name of the dataset as a string to the data function to load the dataset. You can also view the documentation for the data set by passing the show_doc keyword argument."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# data('mpg', show_doc=True) # view the documentation for the dataset\n",
    "# mpg = data('mpg') # load the dataset and store it in a variable\n",
    "# All the datasets loaded from the pydataset library will be pandas dataframes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "metadata": {},
     "execution_count": 10
    }
   ],
   "source": [
    "# 1. Copy the code from the lesson to create a dataframe full of student grades.\n",
    "\n",
    "np.random.seed(123)\n",
    "\n",
    "students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',\n",
    "            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']\n",
    "\n",
    "# randomly generate scores for each student for each subject\n",
    "# note that all the values need to have the same length here\n",
    "math_grades = np.random.randint(low=60, high=100, size=len(students))\n",
    "english_grades = np.random.randint(low=60, high=100, size=len(students))\n",
    "reading_grades = np.random.randint(low=60, high=100, size=len(students))\n",
    "\n",
    "df = pd.DataFrame({'name': students,\n",
    "                   'math': math_grades,\n",
    "                   'english': english_grades,\n",
    "                   'reading': reading_grades})\n",
    "\n",
    "type(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\nRangeIndex: 12 entries, 0 to 11\nData columns (total 4 columns):\n #   Column   Non-Null Count  Dtype \n---  ------   --------------  ----- \n 0   name     12 non-null     object\n 1   math     12 non-null     int64 \n 2   english  12 non-null     int64 \n 3   reading  12 non-null     int64 \ndtypes: int64(3), object(1)\nmemory usage: 512.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "            math    english    reading\n",
       "count  12.000000  12.000000  12.000000\n",
       "mean   84.833333  77.666667  86.500000\n",
       "std    11.134168  13.371158   9.643651\n",
       "min    62.000000  62.000000  67.000000\n",
       "25%    78.500000  63.750000  80.750000\n",
       "50%    90.000000  77.500000  89.000000\n",
       "75%    92.250000  86.750000  93.250000\n",
       "max    98.000000  99.000000  98.000000"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>math</th>\n      <th>english</th>\n      <th>reading</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>12.000000</td>\n      <td>12.000000</td>\n      <td>12.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>84.833333</td>\n      <td>77.666667</td>\n      <td>86.500000</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>11.134168</td>\n      <td>13.371158</td>\n      <td>9.643651</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>62.000000</td>\n      <td>62.000000</td>\n      <td>67.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>78.500000</td>\n      <td>63.750000</td>\n      <td>80.750000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>90.000000</td>\n      <td>77.500000</td>\n      <td>89.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>92.250000</td>\n      <td>86.750000</td>\n      <td>93.250000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>98.000000</td>\n      <td>99.000000</td>\n      <td>98.000000</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 12
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "name       object\n",
       "math        int64\n",
       "english     int64\n",
       "reading     int64\n",
       "dtype: object"
      ]
     },
     "metadata": {},
     "execution_count": 16
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "(12, 4)"
      ]
     },
     "metadata": {},
     "execution_count": 17
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "Index(['name', 'math', 'english', 'reading'], dtype='object')"
      ]
     },
     "metadata": {},
     "execution_count": 18
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "RangeIndex(start=0, stop=12, step=1)"
      ]
     },
     "metadata": {},
     "execution_count": 19
    }
   ],
   "source": [
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "       name  math  english  reading  passing_english\n",
       "0     Sally    62       85       80             True\n",
       "1      Jane    88       79       67             True\n",
       "2     Suzie    94       74       95             True\n",
       "3     Billy    98       96       88             True\n",
       "4       Ada    77       92       98             True\n",
       "5      John    79       76       93             True\n",
       "6    Thomas    82       64       81            False\n",
       "7     Marie    93       63       90            False\n",
       "8    Albert    92       62       87            False\n",
       "9   Richard    69       80       94             True\n",
       "10    Isaac    92       99       93             True\n",
       "11     Alan    92       62       72            False"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>math</th>\n      <th>english</th>\n      <th>reading</th>\n      <th>passing_english</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Sally</td>\n      <td>62</td>\n      <td>85</td>\n      <td>80</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Jane</td>\n      <td>88</td>\n      <td>79</td>\n      <td>67</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Suzie</td>\n      <td>94</td>\n      <td>74</td>\n      <td>95</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Billy</td>\n      <td>98</td>\n      <td>96</td>\n      <td>88</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Ada</td>\n      <td>77</td>\n      <td>92</td>\n      <td>98</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>John</td>\n      <td>79</td>\n      <td>76</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Thomas</td>\n      <td>82</td>\n      <td>64</td>\n      <td>81</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Marie</td>\n      <td>93</td>\n      <td>63</td>\n      <td>90</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Albert</td>\n      <td>92</td>\n      <td>62</td>\n      <td>87</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Richard</td>\n      <td>69</td>\n      <td>80</td>\n      <td>94</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Isaac</td>\n      <td>92</td>\n      <td>99</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>Alan</td>\n      <td>92</td>\n      <td>62</td>\n      <td>72</td>\n      <td>False</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 21
    }
   ],
   "source": [
    "# a. Create a column named passing_english that indicates whether each student has a passing grade in english.\n",
    "\n",
    "df[\"passing_english\"] = df.english > 70\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "       name  math  english  reading  passing_english\n",
       "0     Sally    62       85       80             True\n",
       "1      Jane    88       79       67             True\n",
       "2     Suzie    94       74       95             True\n",
       "3     Billy    98       96       88             True\n",
       "4       Ada    77       92       98             True\n",
       "5      John    79       76       93             True\n",
       "9   Richard    69       80       94             True\n",
       "10    Isaac    92       99       93             True\n",
       "6    Thomas    82       64       81            False\n",
       "7     Marie    93       63       90            False\n",
       "8    Albert    92       62       87            False\n",
       "11     Alan    92       62       72            False"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>math</th>\n      <th>english</th>\n      <th>reading</th>\n      <th>passing_english</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Sally</td>\n      <td>62</td>\n      <td>85</td>\n      <td>80</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Jane</td>\n      <td>88</td>\n      <td>79</td>\n      <td>67</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Suzie</td>\n      <td>94</td>\n      <td>74</td>\n      <td>95</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Billy</td>\n      <td>98</td>\n      <td>96</td>\n      <td>88</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Ada</td>\n      <td>77</td>\n      <td>92</td>\n      <td>98</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>John</td>\n      <td>79</td>\n      <td>76</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Richard</td>\n      <td>69</td>\n      <td>80</td>\n      <td>94</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Isaac</td>\n      <td>92</td>\n      <td>99</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Thomas</td>\n      <td>82</td>\n      <td>64</td>\n      <td>81</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Marie</td>\n      <td>93</td>\n      <td>63</td>\n      <td>90</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Albert</td>\n      <td>92</td>\n      <td>62</td>\n      <td>87</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>Alan</td>\n      <td>92</td>\n      <td>62</td>\n      <td>72</td>\n      <td>False</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 24
    }
   ],
   "source": [
    "# b. Sort the english grades by the passing_english column. How are duplicates handled?\n",
    "\n",
    "df.sort_values(by = \"passing_english\", ascending = False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "       name  math  english  reading  passing_english\n",
       "11     Alan    92       62       72            False\n",
       "8    Albert    92       62       87            False\n",
       "7     Marie    93       63       90            False\n",
       "6    Thomas    82       64       81            False\n",
       "4       Ada    77       92       98             True\n",
       "3     Billy    98       96       88             True\n",
       "10    Isaac    92       99       93             True\n",
       "1      Jane    88       79       67             True\n",
       "5      John    79       76       93             True\n",
       "9   Richard    69       80       94             True\n",
       "0     Sally    62       85       80             True\n",
       "2     Suzie    94       74       95             True"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>math</th>\n      <th>english</th>\n      <th>reading</th>\n      <th>passing_english</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>11</th>\n      <td>Alan</td>\n      <td>92</td>\n      <td>62</td>\n      <td>72</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Albert</td>\n      <td>92</td>\n      <td>62</td>\n      <td>87</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Marie</td>\n      <td>93</td>\n      <td>63</td>\n      <td>90</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Thomas</td>\n      <td>82</td>\n      <td>64</td>\n      <td>81</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Ada</td>\n      <td>77</td>\n      <td>92</td>\n      <td>98</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Billy</td>\n      <td>98</td>\n      <td>96</td>\n      <td>88</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Isaac</td>\n      <td>92</td>\n      <td>99</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Jane</td>\n      <td>88</td>\n      <td>79</td>\n      <td>67</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>John</td>\n      <td>79</td>\n      <td>76</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Richard</td>\n      <td>69</td>\n      <td>80</td>\n      <td>94</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>0</th>\n      <td>Sally</td>\n      <td>62</td>\n      <td>85</td>\n      <td>80</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Suzie</td>\n      <td>94</td>\n      <td>74</td>\n      <td>95</td>\n      <td>True</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 27
    }
   ],
   "source": [
    "# c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)\n",
    "\n",
    "df.sort_values(by = \"name\").sort_values(by = \"passing_english\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "       name  math  english  reading  passing_english\n",
       "8    Albert    92       62       87            False\n",
       "11     Alan    92       62       72            False\n",
       "7     Marie    93       63       90            False\n",
       "6    Thomas    82       64       81            False\n",
       "2     Suzie    94       74       95             True\n",
       "5      John    79       76       93             True\n",
       "1      Jane    88       79       67             True\n",
       "9   Richard    69       80       94             True\n",
       "0     Sally    62       85       80             True\n",
       "4       Ada    77       92       98             True\n",
       "3     Billy    98       96       88             True\n",
       "10    Isaac    92       99       93             True"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>math</th>\n      <th>english</th>\n      <th>reading</th>\n      <th>passing_english</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>8</th>\n      <td>Albert</td>\n      <td>92</td>\n      <td>62</td>\n      <td>87</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>Alan</td>\n      <td>92</td>\n      <td>62</td>\n      <td>72</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Marie</td>\n      <td>93</td>\n      <td>63</td>\n      <td>90</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Thomas</td>\n      <td>82</td>\n      <td>64</td>\n      <td>81</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Suzie</td>\n      <td>94</td>\n      <td>74</td>\n      <td>95</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>John</td>\n      <td>79</td>\n      <td>76</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Jane</td>\n      <td>88</td>\n      <td>79</td>\n      <td>67</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Richard</td>\n      <td>69</td>\n      <td>80</td>\n      <td>94</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>0</th>\n      <td>Sally</td>\n      <td>62</td>\n      <td>85</td>\n      <td>80</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Ada</td>\n      <td>77</td>\n      <td>92</td>\n      <td>98</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Billy</td>\n      <td>98</td>\n      <td>96</td>\n      <td>88</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Isaac</td>\n      <td>92</td>\n      <td>99</td>\n      <td>93</td>\n      <td>True</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 29
    }
   ],
   "source": [
    "# d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step\n",
    "\n",
    "df.sort_values(by = \"passing_english\").sort_values(by = \"english\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "       name  math  english  reading  passing_english  overall_grade\n",
       "0     Sally    62       85       80             True      75.666667\n",
       "1      Jane    88       79       67             True      78.000000\n",
       "2     Suzie    94       74       95             True      87.666667\n",
       "3     Billy    98       96       88             True      94.000000\n",
       "4       Ada    77       92       98             True      89.000000\n",
       "5      John    79       76       93             True      82.666667\n",
       "6    Thomas    82       64       81            False      75.666667\n",
       "7     Marie    93       63       90            False      82.000000\n",
       "8    Albert    92       62       87            False      80.333333\n",
       "9   Richard    69       80       94             True      81.000000\n",
       "10    Isaac    92       99       93             True      94.666667\n",
       "11     Alan    92       62       72            False      75.333333"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>math</th>\n      <th>english</th>\n      <th>reading</th>\n      <th>passing_english</th>\n      <th>overall_grade</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Sally</td>\n      <td>62</td>\n      <td>85</td>\n      <td>80</td>\n      <td>True</td>\n      <td>75.666667</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Jane</td>\n      <td>88</td>\n      <td>79</td>\n      <td>67</td>\n      <td>True</td>\n      <td>78.000000</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Suzie</td>\n      <td>94</td>\n      <td>74</td>\n      <td>95</td>\n      <td>True</td>\n      <td>87.666667</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Billy</td>\n      <td>98</td>\n      <td>96</td>\n      <td>88</td>\n      <td>True</td>\n      <td>94.000000</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Ada</td>\n      <td>77</td>\n      <td>92</td>\n      <td>98</td>\n      <td>True</td>\n      <td>89.000000</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>John</td>\n      <td>79</td>\n      <td>76</td>\n      <td>93</td>\n      <td>True</td>\n      <td>82.666667</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Thomas</td>\n      <td>82</td>\n      <td>64</td>\n      <td>81</td>\n      <td>False</td>\n      <td>75.666667</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Marie</td>\n      <td>93</td>\n      <td>63</td>\n      <td>90</td>\n      <td>False</td>\n      <td>82.000000</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Albert</td>\n      <td>92</td>\n      <td>62</td>\n      <td>87</td>\n      <td>False</td>\n      <td>80.333333</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Richard</td>\n      <td>69</td>\n      <td>80</td>\n      <td>94</td>\n      <td>True</td>\n      <td>81.000000</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Isaac</td>\n      <td>92</td>\n      <td>99</td>\n      <td>93</td>\n      <td>True</td>\n      <td>94.666667</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>Alan</td>\n      <td>92</td>\n      <td>62</td>\n      <td>72</td>\n      <td>False</td>\n      <td>75.333333</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 37
    }
   ],
   "source": [
    "\n",
    "# e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades\n",
    "\n",
    "overall_grade = (df[\"math\"] + df[\"english\"] + df[\"reading\"]) / 3\n",
    "df[\"overall_grade\"] = overall_grade\n",
    "df.sort_values(by = \"overall_grade\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "mpg\n\nPyDataset Documentation (adopted from R Documentation. The displayed examples are in R)\n\n## Fuel economy data from 1999 and 2008 for 38 popular models of car\n\n### Description\n\nThis dataset contains a subset of the fuel economy data that the EPA makes\navailable on http://fueleconomy.gov. It contains only models which had a new\nrelease every year between 1999 and 2008 - this was used as a proxy for the\npopularity of the car.\n\n### Usage\n\n    data(mpg)\n\n### Format\n\nA data frame with 234 rows and 11 variables\n\n### Details\n\n  * manufacturer. \n\n  * model. \n\n  * displ. engine displacement, in litres \n\n  * year. \n\n  * cyl. number of cylinders \n\n  * trans. type of transmission \n\n  * drv. f = front-wheel drive, r = rear wheel drive, 4 = 4wd \n\n  * cty. city miles per gallon \n\n  * hwy. highway miles per gallon \n\n  * fl. \n\n  * class. \n\n\n"
     ]
    }
   ],
   "source": [
    "# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:\n",
    "\n",
    "data('mpg', show_doc = True) # view the documentation for the dataset\n",
    "mpg = data('mpg') # load the dataset and store it in a variable\n",
    "\n",
    "# How many rows and columns are there?\n",
    "# R. 234 rows and 11 columns/variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "manufacturer     object\n",
       "model            object\n",
       "displ           float64\n",
       "year              int64\n",
       "cyl               int64\n",
       "trans            object\n",
       "drv              object\n",
       "cty               int64\n",
       "hwy               int64\n",
       "fl               object\n",
       "class            object\n",
       "dtype: object"
      ]
     },
     "metadata": {},
     "execution_count": 51
    }
   ],
   "source": [
    "# What are the data types of each column?\n",
    "# R. 1) object, 2) object, 3) float64, 4) int64, 5) int64, 6) object, 7) object, 8) int64, 9) int64, 10) object, 11) object\n",
    "mpg.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<bound method NDFrame.describe of     manufacturer   model  displ  year  cyl  ... drv cty  hwy  fl    class\n",
       "1           audi      a4    1.8  1999    4  ...   f  18   29   p  compact\n",
       "2           audi      a4    1.8  1999    4  ...   f  21   29   p  compact\n",
       "3           audi      a4    2.0  2008    4  ...   f  20   31   p  compact\n",
       "4           audi      a4    2.0  2008    4  ...   f  21   30   p  compact\n",
       "5           audi      a4    2.8  1999    6  ...   f  16   26   p  compact\n",
       "..           ...     ...    ...   ...  ...  ...  ..  ..  ...  ..      ...\n",
       "230   volkswagen  passat    2.0  2008    4  ...   f  19   28   p  midsize\n",
       "231   volkswagen  passat    2.0  2008    4  ...   f  21   29   p  midsize\n",
       "232   volkswagen  passat    2.8  1999    6  ...   f  16   26   p  midsize\n",
       "233   volkswagen  passat    2.8  1999    6  ...   f  18   26   p  midsize\n",
       "234   volkswagen  passat    3.6  2008    6  ...   f  17   26   p  midsize\n",
       "\n",
       "[234 rows x 11 columns]>"
      ]
     },
     "metadata": {},
     "execution_count": 52
    }
   ],
   "source": [
    "# Summarize the dataframe with .info and .describe\n",
    "# R. \n",
    "mpg.describe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer   model  displ  year  cyl  ... drv city  hwy  fl    class\n",
       "1           audi      a4    1.8  1999    4  ...   f   18   29   p  compact\n",
       "2           audi      a4    1.8  1999    4  ...   f   21   29   p  compact\n",
       "3           audi      a4    2.0  2008    4  ...   f   20   31   p  compact\n",
       "4           audi      a4    2.0  2008    4  ...   f   21   30   p  compact\n",
       "5           audi      a4    2.8  1999    6  ...   f   16   26   p  compact\n",
       "..           ...     ...    ...   ...  ...  ...  ..  ...  ...  ..      ...\n",
       "230   volkswagen  passat    2.0  2008    4  ...   f   19   28   p  midsize\n",
       "231   volkswagen  passat    2.0  2008    4  ...   f   21   29   p  midsize\n",
       "232   volkswagen  passat    2.8  1999    6  ...   f   16   26   p  midsize\n",
       "233   volkswagen  passat    2.8  1999    6  ...   f   18   26   p  midsize\n",
       "234   volkswagen  passat    3.6  2008    6  ...   f   17   26   p  midsize\n",
       "\n",
       "[234 rows x 11 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>city</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>20</td>\n      <td>31</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(av)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>30</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>230</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>19</td>\n      <td>28</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>231</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>232</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>233</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>234</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>3.6</td>\n      <td>2008</td>\n      <td>6</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>17</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n  </tbody>\n</table>\n<p>234 rows ?? 11 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 54
    }
   ],
   "source": [
    "# Rename the cty column to city.\n",
    "mpg.rename(columns = {'cty': 'city'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer   model  displ  year  cyl  ... drv cty  highway  fl    class\n",
       "1           audi      a4    1.8  1999    4  ...   f  18       29   p  compact\n",
       "2           audi      a4    1.8  1999    4  ...   f  21       29   p  compact\n",
       "3           audi      a4    2.0  2008    4  ...   f  20       31   p  compact\n",
       "4           audi      a4    2.0  2008    4  ...   f  21       30   p  compact\n",
       "5           audi      a4    2.8  1999    6  ...   f  16       26   p  compact\n",
       "..           ...     ...    ...   ...  ...  ...  ..  ..      ...  ..      ...\n",
       "230   volkswagen  passat    2.0  2008    4  ...   f  19       28   p  midsize\n",
       "231   volkswagen  passat    2.0  2008    4  ...   f  21       29   p  midsize\n",
       "232   volkswagen  passat    2.8  1999    6  ...   f  16       26   p  midsize\n",
       "233   volkswagen  passat    2.8  1999    6  ...   f  18       26   p  midsize\n",
       "234   volkswagen  passat    3.6  2008    6  ...   f  17       26   p  midsize\n",
       "\n",
       "[234 rows x 11 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>highway</th>\n      <th>fl</th>\n      <th>class</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>20</td>\n      <td>31</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(av)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>30</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>230</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>19</td>\n      <td>28</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>231</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>232</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>233</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>234</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>3.6</td>\n      <td>2008</td>\n      <td>6</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>17</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n  </tbody>\n</table>\n<p>234 rows ?? 11 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 56
    }
   ],
   "source": [
    "# Rename the hwy column to highway.\n",
    "mpg.rename(columns = {\"hwy\" : \"highway\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer   model  displ  year  cyl  ... drv cty  hwy  fl    class\n",
       "1           audi      a4    1.8  1999    4  ...   f  18   29   p  compact\n",
       "2           audi      a4    1.8  1999    4  ...   f  21   29   p  compact\n",
       "3           audi      a4    2.0  2008    4  ...   f  20   31   p  compact\n",
       "4           audi      a4    2.0  2008    4  ...   f  21   30   p  compact\n",
       "5           audi      a4    2.8  1999    6  ...   f  16   26   p  compact\n",
       "..           ...     ...    ...   ...  ...  ...  ..  ..  ...  ..      ...\n",
       "230   volkswagen  passat    2.0  2008    4  ...   f  19   28   p  midsize\n",
       "231   volkswagen  passat    2.0  2008    4  ...   f  21   29   p  midsize\n",
       "232   volkswagen  passat    2.8  1999    6  ...   f  16   26   p  midsize\n",
       "233   volkswagen  passat    2.8  1999    6  ...   f  18   26   p  midsize\n",
       "234   volkswagen  passat    3.6  2008    6  ...   f  17   26   p  midsize\n",
       "\n",
       "[234 rows x 11 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>20</td>\n      <td>31</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(av)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>30</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>compact</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>230</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>19</td>\n      <td>28</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>231</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>232</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>233</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n    <tr>\n      <th>234</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>3.6</td>\n      <td>2008</td>\n      <td>6</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>17</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n    </tr>\n  </tbody>\n</table>\n<p>234 rows ?? 11 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 57
    }
   ],
   "source": [
    "mpg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer model  displ  year  ...  hwy   fl class  city mileage is superior\n",
       "1            NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "2            NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "3            NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "4            NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "5            NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "..           ...   ...    ...   ...  ...  ...  ...   ...                       ...\n",
       "230          NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "231          NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "232          NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "233          NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "234          NaN   NaN    NaN   NaN  ...  NaN  NaN   NaN                       NaN\n",
       "\n",
       "[234 rows x 12 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n      <th>city mileage is superior</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>230</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>231</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>232</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>233</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>234</th>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n  </tbody>\n</table>\n<p>234 rows ?? 12 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 71
    }
   ],
   "source": [
    "# Do any cars have better city mileage than highway mileage?\n",
    "# R. \n",
    "\n",
    "city_better_than_hwy = np.where(mpg[\"cty\"] > mpg[\"hwy\"], True, False)\n",
    "mpg[\"city mileage is superior\"] = city_better_than_hwy\n",
    "mpg.where(mpg[\"city mileage is superior\"] == True)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "execution_count": 76
    }
   ],
   "source": [
    "(mpg[\"cty\"] > mpg[\"hwy\"]).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer   model  ...  city mileage is superior  mileage_difference\n",
       "1           audi      a4  ...                     False                  11\n",
       "2           audi      a4  ...                     False                   8\n",
       "3           audi      a4  ...                     False                  11\n",
       "4           audi      a4  ...                     False                   9\n",
       "5           audi      a4  ...                     False                  10\n",
       "..           ...     ...  ...                       ...                 ...\n",
       "230   volkswagen  passat  ...                     False                   9\n",
       "231   volkswagen  passat  ...                     False                   8\n",
       "232   volkswagen  passat  ...                     False                  10\n",
       "233   volkswagen  passat  ...                     False                   8\n",
       "234   volkswagen  passat  ...                     False                   9\n",
       "\n",
       "[234 rows x 13 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n      <th>city mileage is superior</th>\n      <th>mileage_difference</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n      <td>False</td>\n      <td>11</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n      <td>False</td>\n      <td>8</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>20</td>\n      <td>31</td>\n      <td>p</td>\n      <td>compact</td>\n      <td>False</td>\n      <td>11</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(av)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>30</td>\n      <td>p</td>\n      <td>compact</td>\n      <td>False</td>\n      <td>9</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>compact</td>\n      <td>False</td>\n      <td>10</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>230</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>19</td>\n      <td>28</td>\n      <td>p</td>\n      <td>midsize</td>\n      <td>False</td>\n      <td>9</td>\n    </tr>\n    <tr>\n      <th>231</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.0</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m6)</td>\n      <td>f</td>\n      <td>21</td>\n      <td>29</td>\n      <td>p</td>\n      <td>midsize</td>\n      <td>False</td>\n      <td>8</td>\n    </tr>\n    <tr>\n      <th>232</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n      <td>False</td>\n      <td>10</td>\n    </tr>\n    <tr>\n      <th>233</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n      <td>False</td>\n      <td>8</td>\n    </tr>\n    <tr>\n      <th>234</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>3.6</td>\n      <td>2008</td>\n      <td>6</td>\n      <td>auto(s6)</td>\n      <td>f</td>\n      <td>17</td>\n      <td>26</td>\n      <td>p</td>\n      <td>midsize</td>\n      <td>False</td>\n      <td>9</td>\n    </tr>\n  </tbody>\n</table>\n<p>234 rows ?? 13 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 78
    }
   ],
   "source": [
    "# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.\n",
    "\n",
    "mpg[\"mileage_difference\"] = (mpg[\"hwy\"] - mpg[\"cty\"])\n",
    "mpg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer       model  ...  city mileage is superior  mileage_difference\n",
       "107        honda       civic  ...                     False                  12\n",
       "223   volkswagen  new beetle  ...                     False                  12\n",
       "1           audi          a4  ...                     False                  11\n",
       "229   volkswagen      passat  ...                     False                  11\n",
       "36     chevrolet      malibu  ...                     False                  11\n",
       "\n",
       "[5 rows x 13 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n      <th>city mileage is superior</th>\n      <th>mileage_difference</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>107</th>\n      <td>honda</td>\n      <td>civic</td>\n      <td>1.8</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>24</td>\n      <td>36</td>\n      <td>c</td>\n      <td>subcompact</td>\n      <td>False</td>\n      <td>12</td>\n    </tr>\n    <tr>\n      <th>223</th>\n      <td>volkswagen</td>\n      <td>new beetle</td>\n      <td>1.9</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l4)</td>\n      <td>f</td>\n      <td>29</td>\n      <td>41</td>\n      <td>d</td>\n      <td>subcompact</td>\n      <td>False</td>\n      <td>12</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>audi</td>\n      <td>a4</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>29</td>\n      <td>p</td>\n      <td>compact</td>\n      <td>False</td>\n      <td>11</td>\n    </tr>\n    <tr>\n      <th>229</th>\n      <td>volkswagen</td>\n      <td>passat</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l5)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>29</td>\n      <td>p</td>\n      <td>midsize</td>\n      <td>False</td>\n      <td>11</td>\n    </tr>\n    <tr>\n      <th>36</th>\n      <td>chevrolet</td>\n      <td>malibu</td>\n      <td>3.5</td>\n      <td>2008</td>\n      <td>6</td>\n      <td>auto(l4)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>29</td>\n      <td>r</td>\n      <td>midsize</td>\n      <td>False</td>\n      <td>11</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 96
    }
   ],
   "source": [
    "# Which car (or cars) has the highest mileage difference?\n",
    "\n",
    "mpg.sort_values(by = \"mileage_difference\", ascending = False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer  model  displ  year  cyl     trans drv  cty  hwy fl    class\n",
       "220   volkswagen  jetta    2.8  1999    6  auto(l4)   f   16   23  r  compact"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>220</th>\n      <td>volkswagen</td>\n      <td>jetta</td>\n      <td>2.8</td>\n      <td>1999</td>\n      <td>6</td>\n      <td>auto(l4)</td>\n      <td>f</td>\n      <td>16</td>\n      <td>23</td>\n      <td>r</td>\n      <td>compact</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 111
    }
   ],
   "source": [
    "# Which compact class car has the lowest highway mileage? The best?\n",
    "\n",
    "mpg[mpg[\"class\"] == \"compact\"].sort_values(by = \"hwy\").head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer  model  displ  year  cyl       trans drv  cty  hwy fl    class\n",
       "213   volkswagen  jetta    1.9  1999    4  manual(m5)   f   33   44  d  compact"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>213</th>\n      <td>volkswagen</td>\n      <td>jetta</td>\n      <td>1.9</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>33</td>\n      <td>44</td>\n      <td>d</td>\n      <td>compact</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 113
    }
   ],
   "source": [
    "# Which compact class car has the lowest highway mileage? The best?\n",
    "\n",
    "mpg[mpg[\"class\"] == \"compact\"].sort_values(by = \"hwy\", ascending = False).head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    manufacturer                model  displ  year  ...  hwy fl       class  average\n",
       "222   volkswagen           new beetle    1.9  1999  ...   44  d  subcompact     39.5\n",
       "213   volkswagen                jetta    1.9  1999  ...   44  d     compact     38.5\n",
       "223   volkswagen           new beetle    1.9  1999  ...   41  d  subcompact     35.0\n",
       "197       toyota              corolla    1.8  2008  ...   37  r     compact     32.5\n",
       "196       toyota              corolla    1.8  1999  ...   35  r     compact     30.5\n",
       "..           ...                  ...    ...   ...  ...  ... ..         ...      ...\n",
       "127         jeep   grand cherokee 4wd    4.7  2008  ...   12  e         suv     10.5\n",
       "60         dodge          durango 4wd    4.7  2008  ...   12  e         suv     10.5\n",
       "66         dodge  ram 1500 pickup 4wd    4.7  2008  ...   12  e      pickup     10.5\n",
       "70         dodge  ram 1500 pickup 4wd    4.7  2008  ...   12  e      pickup     10.5\n",
       "55         dodge    dakota pickup 4wd    4.7  2008  ...   12  e      pickup     10.5\n",
       "\n",
       "[234 rows x 12 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n      <th>average</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>222</th>\n      <td>volkswagen</td>\n      <td>new beetle</td>\n      <td>1.9</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>35</td>\n      <td>44</td>\n      <td>d</td>\n      <td>subcompact</td>\n      <td>39.5</td>\n    </tr>\n    <tr>\n      <th>213</th>\n      <td>volkswagen</td>\n      <td>jetta</td>\n      <td>1.9</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>33</td>\n      <td>44</td>\n      <td>d</td>\n      <td>compact</td>\n      <td>38.5</td>\n    </tr>\n    <tr>\n      <th>223</th>\n      <td>volkswagen</td>\n      <td>new beetle</td>\n      <td>1.9</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l4)</td>\n      <td>f</td>\n      <td>29</td>\n      <td>41</td>\n      <td>d</td>\n      <td>subcompact</td>\n      <td>35.0</td>\n    </tr>\n    <tr>\n      <th>197</th>\n      <td>toyota</td>\n      <td>corolla</td>\n      <td>1.8</td>\n      <td>2008</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>28</td>\n      <td>37</td>\n      <td>r</td>\n      <td>compact</td>\n      <td>32.5</td>\n    </tr>\n    <tr>\n      <th>196</th>\n      <td>toyota</td>\n      <td>corolla</td>\n      <td>1.8</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>manual(m5)</td>\n      <td>f</td>\n      <td>26</td>\n      <td>35</td>\n      <td>r</td>\n      <td>compact</td>\n      <td>30.5</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>127</th>\n      <td>jeep</td>\n      <td>grand cherokee 4wd</td>\n      <td>4.7</td>\n      <td>2008</td>\n      <td>8</td>\n      <td>auto(l5)</td>\n      <td>4</td>\n      <td>9</td>\n      <td>12</td>\n      <td>e</td>\n      <td>suv</td>\n      <td>10.5</td>\n    </tr>\n    <tr>\n      <th>60</th>\n      <td>dodge</td>\n      <td>durango 4wd</td>\n      <td>4.7</td>\n      <td>2008</td>\n      <td>8</td>\n      <td>auto(l5)</td>\n      <td>4</td>\n      <td>9</td>\n      <td>12</td>\n      <td>e</td>\n      <td>suv</td>\n      <td>10.5</td>\n    </tr>\n    <tr>\n      <th>66</th>\n      <td>dodge</td>\n      <td>ram 1500 pickup 4wd</td>\n      <td>4.7</td>\n      <td>2008</td>\n      <td>8</td>\n      <td>auto(l5)</td>\n      <td>4</td>\n      <td>9</td>\n      <td>12</td>\n      <td>e</td>\n      <td>pickup</td>\n      <td>10.5</td>\n    </tr>\n    <tr>\n      <th>70</th>\n      <td>dodge</td>\n      <td>ram 1500 pickup 4wd</td>\n      <td>4.7</td>\n      <td>2008</td>\n      <td>8</td>\n      <td>manual(m6)</td>\n      <td>4</td>\n      <td>9</td>\n      <td>12</td>\n      <td>e</td>\n      <td>pickup</td>\n      <td>10.5</td>\n    </tr>\n    <tr>\n      <th>55</th>\n      <td>dodge</td>\n      <td>dakota pickup 4wd</td>\n      <td>4.7</td>\n      <td>2008</td>\n      <td>8</td>\n      <td>auto(l5)</td>\n      <td>4</td>\n      <td>9</td>\n      <td>12</td>\n      <td>e</td>\n      <td>pickup</td>\n      <td>10.5</td>\n    </tr>\n  </tbody>\n</table>\n<p>234 rows ?? 12 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 115
    }
   ],
   "source": [
    "# Create a column named average_mileage that is the mean of the city and highway mileage.\n",
    "\n",
    "mpg[\"average\"] = (mpg[\"hwy\"] + mpg[\"cty\"]) / 2\n",
    "mpg.sort_values(by = \"average\", ascending = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "   manufacturer        model  displ  year  cyl  ... cty hwy  fl    class average\n",
       "38        dodge  caravan 2wd    2.4  1999    4  ...  18  24   r  minivan    21.0\n",
       "\n",
       "[1 rows x 12 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>manufacturer</th>\n      <th>model</th>\n      <th>displ</th>\n      <th>year</th>\n      <th>cyl</th>\n      <th>trans</th>\n      <th>drv</th>\n      <th>cty</th>\n      <th>hwy</th>\n      <th>fl</th>\n      <th>class</th>\n      <th>average</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>38</th>\n      <td>dodge</td>\n      <td>caravan 2wd</td>\n      <td>2.4</td>\n      <td>1999</td>\n      <td>4</td>\n      <td>auto(l3)</td>\n      <td>f</td>\n      <td>18</td>\n      <td>24</td>\n      <td>r</td>\n      <td>minivan</td>\n      <td>21.0</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 117
    }
   ],
   "source": [
    "# Which dodge car has the best average mileage? The worst?\n",
    "\n",
    "mpg[mpg[\"manufacturer\"] == \"dodge\"].sort_values(by = \"average\", ascending = False).head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Mammals\n\nPyDataset Documentation (adopted from R Documentation. The displayed examples are in R)\n\n## Garland(1983) Data on Running Speed of Mammals\n\n### Description\n\nObservations on the maximal running speed of mammal species and their body\nmass.\n\n### Usage\n\n    data(Mammals)\n\n### Format\n\nA data frame with 107 observations on the following 4 variables.\n\nweight\n\nBody mass in Kg for \"typical adult sizes\"\n\nspeed\n\nMaximal running speed (fastest sprint velocity on record)\n\nhoppers\n\nlogical variable indicating animals that ambulate by hopping, e.g. kangaroos\n\nspecials\n\nlogical variable indicating special animals with \"lifestyles in which speed\ndoes not figure as an important factor\": Hippopotamus, raccoon (Procyon),\nbadger (Meles), coati (Nasua), skunk (Mephitis), man (Homo), porcupine\n(Erithizon), oppossum (didelphis), and sloth (Bradypus)\n\n### Details\n\nUsed by Chappell (1989) and Koenker, Ng and Portnoy (1994) to illustrate the\nfitting of piecewise linear curves.\n\n### Source\n\nGarland, T. (1983) The relation between maximal running speed and body mass in\nterrestrial mammals, _J. Zoology_, 199, 1557-1570.\n\n### References\n\nKoenker, R., P. Ng and S. Portnoy, (1994) Quantile Smoothing Splines???\n_Biometrika_, 81, 673-680.\n\nChappell, R. (1989) Fitting Bent Lines to Data, with Applications ot\nAllometry, _J. Theo. Biology_, 138, 235-256.\n\n### See Also\n\n`rqss`\n\n### Examples\n\n    data(Mammals)\n    attach(Mammals)\n    x <- log(weight)\n    y <- log(speed)\n    plot(x,y, xlab=\"Weight in log(Kg)\", ylab=\"Speed in log(Km/hour)\",type=\"n\")\n    points(x[hoppers],y[hoppers],pch = \"h\", col=\"red\")\n    points(x[specials],y[specials],pch = \"s\", col=\"blue\")\n    others <- (!hoppers & !specials)\n    points(x[others],y[others], col=\"black\",cex = .75)\n    fit <- rqss(y ~ qss(x, lambda = 1),tau = .9)\n    plot(fit)\n\n\n"
     ]
    }
   ],
   "source": [
    "# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:\n",
    "\n",
    "data(\"Mammals\", show_doc = True)\n",
    "mammals = data(\"Mammals\")\n",
    "\n",
    "# How many rows and columns are there?\n",
    "# R. 107 row, and 4 columns/variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "weight      float64\n",
       "speed       float64\n",
       "hoppers        bool\n",
       "specials       bool\n",
       "dtype: object"
      ]
     },
     "metadata": {},
     "execution_count": 121
    }
   ],
   "source": [
    "# What are the data types?\n",
    "\n",
    "mammals.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<bound method DataFrame.info of        weight  speed  hoppers  specials\n",
       "1    6000.000   35.0    False     False\n",
       "2    4000.000   26.0    False     False\n",
       "3    3000.000   25.0    False     False\n",
       "4    1400.000   45.0    False     False\n",
       "5     400.000   70.0    False     False\n",
       "6     350.000   70.0    False     False\n",
       "7     300.000   64.0    False     False\n",
       "8     260.000   70.0    False     False\n",
       "9     250.000   40.0    False     False\n",
       "10   3800.000   25.0    False      True\n",
       "11   1000.000   60.0    False     False\n",
       "12    900.000   70.0    False     False\n",
       "13    900.000   56.0    False     False\n",
       "14    800.000   29.0    False     False\n",
       "15    750.000   57.0    False     False\n",
       "16    500.000   32.0    False     False\n",
       "17    450.000   56.0    False     False\n",
       "18    300.000   72.0    False     False\n",
       "19    300.000   90.0    False     False\n",
       "20    250.000   80.0    False     False\n",
       "21    250.000   56.0    False     False\n",
       "22    170.000   80.0    False     False\n",
       "23    150.000   48.0    False     False\n",
       "24    130.000   70.0    False     False\n",
       "25    120.000   80.0    False     False\n",
       "26    120.000   61.0    False     False\n",
       "27    110.000   33.0    False     False\n",
       "28    100.000   64.0    False     False\n",
       "29     85.000   55.0    False     False\n",
       "30     80.000   65.0    False     False\n",
       "31     72.000   56.0    False     False\n",
       "32     70.000   45.0    False     False\n",
       "33     65.000   60.0    False     False\n",
       "34     62.000   81.0    False     False\n",
       "35     50.000  100.0    False     False\n",
       "36     50.000   60.0    False     False\n",
       "37     50.000   40.0    False     False\n",
       "38     50.000   47.0    False     False\n",
       "39     37.000  105.0    False     False\n",
       "40     35.000   80.0    False     False\n",
       "41     34.000   97.0    False     False\n",
       "42     30.000   97.0    False     False\n",
       "43     30.000   80.0    False     False\n",
       "44     30.000   45.0    False     False\n",
       "45     20.000   81.0    False     False\n",
       "46    400.000   40.0    False     False\n",
       "47    300.000   48.0    False     False\n",
       "48    230.000   56.0    False     False\n",
       "49    150.000   59.0    False     False\n",
       "50    135.000   48.0    False     False\n",
       "51     65.000   65.0    False     False\n",
       "52     60.000   60.0    False     False\n",
       "53     55.000  110.0    False     False\n",
       "54     45.000   50.0    False     False\n",
       "55     40.000   64.0    False     False\n",
       "56     25.000   67.0    False     False\n",
       "57     20.000   70.0    False     False\n",
       "58     16.000   65.0    False     False\n",
       "59     12.000   24.0    False      True\n",
       "60     11.000   30.0    False      True\n",
       "61     10.000   56.0    False     False\n",
       "62      7.000   60.0    False     False\n",
       "63      6.000   72.0    False     False\n",
       "64      5.000   64.0    False     False\n",
       "65      5.000   27.0    False      True\n",
       "66      3.000   16.0    False      True\n",
       "67    127.000   32.0    False     False\n",
       "68     70.000   40.0    False      True\n",
       "69     13.000   37.0    False      True\n",
       "70      9.000    3.2    False      True\n",
       "71      4.000   16.0    False     False\n",
       "72      0.600   36.0    False     False\n",
       "73      0.600   20.0    False     False\n",
       "74      0.550   27.0    False     False\n",
       "75      0.500   18.0    False     False\n",
       "76      0.400   20.0    False     False\n",
       "77      0.300   13.0    False     False\n",
       "78      0.250    9.7    False     False\n",
       "79      0.220   15.0    False     False\n",
       "80      0.110    9.0    False     False\n",
       "81      0.100   17.0    False     False\n",
       "82      0.056   21.0     True     False\n",
       "83      0.050   11.0    False     False\n",
       "84      0.045   16.0    False     False\n",
       "85      0.035   32.0     True     False\n",
       "86      0.035   14.0     True     False\n",
       "87      0.030    6.8    False     False\n",
       "88      0.030    9.1    False     False\n",
       "89      0.025   11.0    False     False\n",
       "90      0.025    8.6    False     False\n",
       "91      0.018    8.9    False     False\n",
       "92      0.016   13.0    False     False\n",
       "93      0.100    4.0    False     False\n",
       "94      0.100    2.4    False     False\n",
       "95      0.016    3.6    False     False\n",
       "96      4.600   64.0     True     False\n",
       "97      4.400   72.0     True     False\n",
       "98      4.000   72.0     True     False\n",
       "99      3.500   56.0     True     False\n",
       "100     2.000   64.0     True     False\n",
       "101     1.900   56.0     True     False\n",
       "102     1.500   50.0     True     False\n",
       "103     1.500   40.0     True     False\n",
       "104    50.000   65.0    False     False\n",
       "105     5.000    7.4    False      True\n",
       "106     0.024   13.0    False     False\n",
       "107     4.000    1.6    False      True>"
      ]
     },
     "metadata": {},
     "execution_count": 122
    }
   ],
   "source": [
    "# Summarize the dataframe with .info and .describe\n",
    "\n",
    "mammals.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    weight  speed  hoppers  specials\n",
       "53    55.0  110.0    False     False"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>weight</th>\n      <th>speed</th>\n      <th>hoppers</th>\n      <th>specials</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>53</th>\n      <td>55.0</td>\n      <td>110.0</td>\n      <td>False</td>\n      <td>False</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 124
    }
   ],
   "source": [
    "# What is the the weight of the fastest animal?\n",
    "# R. 55.0\n",
    "\n",
    "mammals.sort_values(by = \"speed\", ascending = False).head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "10.0"
      ]
     },
     "metadata": {},
     "execution_count": 5
    }
   ],
   "source": [
    "# What is the overal percentage of specials?\n",
    "\n",
    "rows_w_specials = len(mammals[mammals[\"specials\"] == True].index)\n",
    "overall_percentage = rows_w_specials / len([mammals[\"specials\"]])\n",
    "overall_percentage\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# How many animals are hoppers that are above the median speed? What percentage is this?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "     weight  speed  hoppers  specials\n",
       "97    4.400   72.0     True     False\n",
       "98    4.000   72.0     True     False\n",
       "96    4.600   64.0     True     False\n",
       "100   2.000   64.0     True     False\n",
       "99    3.500   56.0     True     False\n",
       "101   1.900   56.0     True     False\n",
       "102   1.500   50.0     True     False\n",
       "103   1.500   40.0     True     False\n",
       "85    0.035   32.0     True     False\n",
       "82    0.056   21.0     True     False\n",
       "86    0.035   14.0     True     False"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>weight</th>\n      <th>speed</th>\n      <th>hoppers</th>\n      <th>specials</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>97</th>\n      <td>4.400</td>\n      <td>72.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>98</th>\n      <td>4.000</td>\n      <td>72.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>96</th>\n      <td>4.600</td>\n      <td>64.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>100</th>\n      <td>2.000</td>\n      <td>64.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>99</th>\n      <td>3.500</td>\n      <td>56.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>101</th>\n      <td>1.900</td>\n      <td>56.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>102</th>\n      <td>1.500</td>\n      <td>50.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>103</th>\n      <td>1.500</td>\n      <td>40.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>85</th>\n      <td>0.035</td>\n      <td>32.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>82</th>\n      <td>0.056</td>\n      <td>21.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>86</th>\n      <td>0.035</td>\n      <td>14.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 17
    }
   ],
   "source": [
    "# Finding all the Mammals that fall in the category of \"hoppers\"\n",
    "\n",
    "all_hoppers = mammals[mammals[\"hoppers\"] == True].sort_values(by = \"speed\", ascending = False)\n",
    "all_hoppers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "48.0"
      ]
     },
     "metadata": {},
     "execution_count": 16
    }
   ],
   "source": [
    "# Finding the \"speed\" median for all Mammals included in the Dataframe\n",
    "\n",
    "the_median = mammals[\"speed\"].median()\n",
    "the_median"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "     weight  speed  hoppers  specials\n",
       "97      4.4   72.0     True     False\n",
       "98      4.0   72.0     True     False\n",
       "96      4.6   64.0     True     False\n",
       "100     2.0   64.0     True     False\n",
       "99      3.5   56.0     True     False\n",
       "101     1.9   56.0     True     False\n",
       "102     1.5   50.0     True     False"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>weight</th>\n      <th>speed</th>\n      <th>hoppers</th>\n      <th>specials</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>97</th>\n      <td>4.4</td>\n      <td>72.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>98</th>\n      <td>4.0</td>\n      <td>72.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>96</th>\n      <td>4.6</td>\n      <td>64.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>100</th>\n      <td>2.0</td>\n      <td>64.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>99</th>\n      <td>3.5</td>\n      <td>56.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>101</th>\n      <td>1.9</td>\n      <td>56.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>102</th>\n      <td>1.5</td>\n      <td>50.0</td>\n      <td>True</td>\n      <td>False</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 18
    }
   ],
   "source": [
    "# Finding all the Mammals that fall in the \"hoppers\" category and that register a \"speed\" greater than the total median for all Mammals in the Dataframe\n",
    "\n",
    "fast_hoppers = mammals.loc[(mammals[\"speed\"] > the_median) & (mammals[\"hoppers\"] == True)].sort_values(by = \"speed\", ascending = False)\n",
    "fast_hoppers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "63.63636363636363"
      ]
     },
     "metadata": {},
     "execution_count": 21
    }
   ],
   "source": [
    "# Determining the percentage of \"hoppers\" that beat the median \"speed\" of all Mammals in Dataframe, in relation to all Mammals that fall in the \"hoppers\" category\n",
    "\n",
    "percentage_of_fast_hoppers = (len(fast_hoppers) / len(all_hoppers)) * 100\n",
    "percentage_of_fast_hoppers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "6.5420560747663545"
      ]
     },
     "metadata": {},
     "execution_count": 23
    }
   ],
   "source": [
    "# Determining the percentage of \"hoppers\" that beat the median \"speed\" of all Mammals in Dataframe, in relation to all Mammals in Dataframe\n",
    "\n",
    "fastest_hoppers_in_mammals_kingdom = (len(fast_hoppers) / len(mammals)) * 100\n",
    "fastest_hoppers_in_mammals_kingdom"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}