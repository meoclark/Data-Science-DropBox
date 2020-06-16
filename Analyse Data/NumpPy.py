# Introduction to NumPy: Numerical Python
#NumPy is great at storing and manipulating numerical data in arrays.

import numpy as np

# NumPy Arrays

#A NumPy array is a special type of list. It’s a data structure that organizes multiple items. Each item can be of any type (strings, numbers, or even other arrays).

test_1 = np.array([92, 94, 88, 91, 87])

# test_1 is now a numpy array

#Creating an Array from a CSV
# Note the delimiter can be in other formats such as semi colon and tabs.

test_2 = np.genfromtxt('test_2.csv', delimiter=',')


# Operations with NumPy Arrays


# Let’s compare how to add a number to each value in a python list versus a NumPy array:
# With a list
A = [1, 2, 3, 4, 5,6]
A_plus_3 = []
for i in range(len(A)):
    l_plus_3.append(A[i] + 3)
# With an array
a = np.array(l)
a_plus_3 = a + 3

#Squaring each value:
a ** 2
#array([ 1,  4,  9, 16, 25, 36])

#Taking the square root of each value:

np.sqrt(a)
#array([ 1, 1.41421356, 1.73205081, 2, 2.23606798, 2.44948974])

# Add extra 2 points to test_3
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2


# Operations with NumPy Arrays II

# Arrays can also be added to or subtracted from each other in NumPy, 
# assuming the arrays have the same number of elements.

 a = np.array([1, 2, 3, 4, 5])
 b = np.array([6, 7, 8, 9, 10])
 a + b
#array([ 7,  9, 11, 13, 15])



test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

total_grade = test_1 + test_2 + test_3_fixed
# average score
final_grade = total_grade / 3
print(final_grade)


# Two-Dimensional Arrays
# in NumPy we can create an array of arrays.
# If the arrays that make up our bigger array are all the same size, then it has a special name: a two-dimensional array.

#we could have also stored all of this data in a single, two-dimensional array: Notice the double square brackets syntax [[]]

np.array([[92, 94, 88, 91, 87], 
          [79, 100, 86, 93, 91],
          [87, 85, 72, 90, 92]])

coin_toss_again = np.array([[1,0,0,1,0],[0,0,1,1,1]])


# Selecting Elements from a 1-D Array
# This uses normal indexing
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[-2]
#grabs 93

manual_adwoa_test_1 = test_1[1:3]
# grabs 94 88


# Selecting Elements from a 2-D Array

# The syntax for selecting from a 2-d array is a[row,column] where a is the array.

a = np.array([[32, 15, 6, 9, 14], 
              [12, 10, 5, 23, 1],
              [2, 16, 13, 40, 37]])
a[2,1]
#16

# selects the first column
a[:,0]
#array([32, 12,  2])

a[1,:]
#array([12, 10,  5, 23,  1])

# selects the first three elements of the first row
a[0,0:3]
#array([32, 15,  6])

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2,0]

cody_test_scores = student_scores[:,4]


# Logical Operations with Arrays

# < > == != | &

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]

hot = porridge[porridge > 80]

just_right = porridge[(porridge >= 60) & (porridge <= 80)]

print(cold,
hot,
just_right
)

# Review 

import numpy as np

temperatures = np.genfromtxt('temperature_data.csv',delimiter=',')

print(temperatures)

temperatures_fixed = temperatures + 3.0
monday_temperatures = temperatures_fixed[0,:]
thursday_friday_morning = temperatures_fixed[3:,1]

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]

 # Project Bettys Bakery

 import numpy as np
cupcakes = np.array([2,0.75,2,1,0.5])

recipes = np.genfromtxt('recipes.csv',delimiter=',')

print(recipes)

eggs = recipes[:,2]

print(eggs)

#egg = recipes[recipes[:,2] == 1]

cookies = recipes[2,:]
print(cookies)

double_batch = cupcakes * 2
print(double_batch)

grocery_list = cookies + double_batch
print(grocery_list)

