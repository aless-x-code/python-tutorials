# lists
string1 = "hello"
float1 = 5.7
list1 = ["metro", True, 3.4, 5, string1, float1, [4, "kilo"]]
list2 = [['hallway', 11.25], ['kitchen', 18.0], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5]]

# list extract elements
list1[0]
list1[-1]
calculation = list1[3] + list2[-3]
extract_list = [list2[2][1]] #20.0


# list slicing
# x[start:end] END won't be included
slicing1 = list1[0:2]
slicing2 = list2[2:] # 2: and forward
slicing3 = list2[:3] # beggining to :3

#List manipulation (chnage, add, remove)
# change
list1 = ["metro", True, 3.4, 5, string1, float1, [4, "kilo"]]
list1[-1][1] = "pounds"
list1[2:4] = 7.9, 8


areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas
areas_copy[0] = 5.0
# [5.0, 18.0, 20.0, 10.75, 9.50]

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas) #prevents areas(original from being modfied)
areas_copy[0] = 5.0
# [11.25, 18.0, 20.0, 10.75, 9.50]

# add
new_list = list1 + [9.9, "milimeters"] # will be added to the end
# delete
del(new_list[0]); del(new_list[1]) # metro and True
# ALL INDEXES WILL BE MOFIFIED AFTER THE DEL COMMAND, NOT BEFORE 

# Help! ; information on a function
# ?function or help(function)
help(sorted)

# Sorted function
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second
full_sorted = sorted(full, reverse=True)

# Methods
# synthax = x.method
place = "house"
place_up = place.upper()
print(place.count("h"))

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20.0)) #What is the index #?
areas.append(24.5); areas.append(15.45) 
areas.reverse() # reverse the order hereafter

print(areas.shape) # row x col

# Packages
import math # math package (pi, square, etc)
r = 0.43 # represent radius
C = 2 * r * math.pi # circumference
A = math.pi * r ** 2 #a rea
print("Circumference: " + str(C))
print("Area: " + str(A))

from math import radians # selective import
dist = r * radians(12) 

# selective import
#from scipy > linalg > inv()
# from scipy.linalg import inv as my_inv 

# NumPy, data science package
# list can't contain different types, they will converted to change (type coercion)
# Type coercion = True=1 False=0
# + - * / have different meanings. 
array1 = [1, True, 3]
array2 = [3, 3, False]
np_array1 = np.array(array1)
np_array2 = np.array(array2)
np_sum = np_array1 + np_array2 
# [4 4 3]

# * 
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
array([[ 2,  4],
       [ 6,  8],
       [10, 12]])
np_mat + np.array([10, 10])
array([[11, 12],
       [13, 14],
       [15, 16]])
np_mat + np_mat
array([[ 2,  4],
       [ 6,  8],
       [10, 12]])






# array function
import numpy as np
list4 = [11.25, 18.0, 20.0, 10.75, 9.50]
array1 = np.array(list4)

# Array exercise, BMI
height_in = [11.25, 18.0, 20.0, 10.75, 9.50]
weight_lb = [180, 215, 210, 210, 188, 176]
np_height_m = np.array(height_in) * 0.0254 # convert height into an array, then into meters
np_weight_kg = np.array(weight_lb) * 0.453592 # convert weight into an array, then into kg
bmi = np_weight_kg / (np_height_m ** 2) # bmi formula

# Boolean NumPy arrays
light = bmi < 21 # boolean validation of bmi elements 
print(light) # will print all elements, and indicate T/F for each
# [False False True True]
print(bmi[light]) #print bmi elements whose value is true in light
# [20.89 20.99 18.88] 

# Array indexing
# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]
# ["a", "c"]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0] # all rows, column 0
# ["a", "c"]
















