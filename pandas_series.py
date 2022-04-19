import numpy as np
import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
vowels = list('aeiou')

# Exercises I
# 1) Determine the number of elements in fruits.
fruits.shape[0]
print(fruits.shape[0])

fruits.size #alt
len(fruits) #alt

#2) Output only the index from fruits.

# 3) Output only the values from fruits.

fruits.values #brings back a numpy array. Pandas built on numpy

# 4) Confirm the data type of the values in fruits.
fruits.dtype #o for object

# 5) Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

fruits.head()
fruits.tail(3)
fruits.sample(2)

# 6) Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()

# 7) Run the code necessary to produce only the unique string values from fruits.
fruits.unique

# 8) Determine how many times each unique string value occurs in fruits.
fruits.value_counts()

# 9) Determine the string value that occurs most frequently in fruits.
fruits.value_counts().head(1)

#use n largest
fruits.value_counts().nlargest(n = 1)

#can also use idxmax
fruits.value_counts().idxmax()

# 10) Determine the string value that occurs least frequently in fruits.

fruits.value_counts().nsmallest(n = 1, keep = 'all') #need to keep all so don't lose all the unique single values

# Exercises II

# 1) Capitalize all the string values in fruits.

fruits.str.capitalize()
print(fruits.str.capitalize())

# 2) Count the letter "a" in all the string values (use string vectorization).

fruits.str.count('a')
print(fruits.str.count('a'))

# 3) Output the number of vowels in each and every string value.
def vowel_count(fruits):
    return len([x for x in fruits.lower() if x in vowels]) #use list comprehension since vowels already defined
fruits.apply(vowel_count)

# 3) better, stronger, faster alt
vowels_counts = fruits.str.lower().str.count(r'[aeiou]') 
print(vowels_counts)

# 3) as a dataframe

fruits_vowels = pd.DataFrame({'fruits' : fruits, 'Number of vowels' : vowels_counts})
print(fruits_vowels)

# 4) Write the code to get the longest string value from fruits

max(fruits, key = len)
print(max(fruits, key = len))

# 4) using boolean mask and indexing
longest_fruit_name = fruits.str.len().max() #use max to get max length of series elements
fruits_booleans = fruits.str.len() == longest_fruit_name 
fruits_booleans #when run @ index 5

#index
print(fruits[fruits_booleans]) #honeycrisp apple


# 5) Write the code to get the string values with 5 or more letters in the name.

fruits[fruits.str.len() >= 5] 
print(fruits[fruits.str.len() >= 5])

# 6) Use the .apply method with a lambda function to find the fruit(s) 
# containing the letter "o" two or more times.

fruits[fruits.apply(lambda fruits: fruits.count('o') > 1)]
print(fruits[fruits.apply(lambda fruits: fruits.count('o') > 1)])

# 7) Write the code to get only the string values containing the substring "berry".

fruits[fruits.str.contains('berry')]
print(fruits[fruits.str.contains('berry')])

# 8) Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]
print(fruits[fruits.str.contains('apple')])

# 9) Which string value contains the most vowels?

most_vowels = (fruits.str.count(r'[aeiou]')).max() #5

most_vowels_boolean = fruits.str.count(r'[aeiou]') == most_vowels #use this faster method from ques 3 and assign to new variable

fruits[most_vowels_boolean] #index
print(fruits[most_vowels_boolean])