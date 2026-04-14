import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 0]])
arr3 = np.array([10, 20, 30, 40, 50])
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
identity = np.eye(3)
random_arr = np.random.rand(3, 3)

""" print(arr1)
print(arr2)
print(zeros)
print(ones)
print(identity)
print(random_arr) """

# Array properties
""" print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Datatype:", arr2.dtype)
print("Dimensions:", arr2.ndim)  """

# Indexing & Slicing
""" print("First row:", arr2[0])
print("Element at (1,2):", arr2[1,2])
print("Sliced array:", arr1[1:4])
a=np.array([[[1, 2, 3, 4, 5],[2,4,6,8,9]]])
print(a[0,1,2]) """

# Reshaping & Transposing
""" reshaped = arr1.reshape(5, 1)
transposed = arr2.T
print("Reshaped:", reshaped)
print("Transposed:", transposed) """

# Mathematical Operations
""" sum_arr = arr1 + arr3
prod_arr = arr1 * arr3
div_arr = arr3 / arr1
sqrt_arr = np.sqrt(arr3)
power_arr = np.power(arr1, 3)
print("Sum:", sum_arr)
print("Product:", prod_arr)
print("Division:", div_arr)
print("Square Root:", sqrt_arr)
print("Power:", power_arr) """


from scipy import stats
# Statistical Functions
arr3 = np.array([10, 20, 30, 40, 50, 20])
mean_val = np.mean(arr3)
median_val = np.median(arr3)
mode_val = stats.mode(arr3)
std_dev = np.std(arr3)
var_val = np.var(arr3)
min_val = np.min(arr3)
max_val = np.max(arr3)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
print("Mode:", mode_val)
print("Variance:", var_val)
print("Min:", min_val)
print("Max:", max_val)
# Concatenation & Stacking
concat_arr = np.concatenate((arr1, arr3))
stacked_arr = np.vstack((arr1, arr3))
print("Concatenated:", concat_arr)
print("Stacked:", stacked_arr)

# Linear Algebra
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print(matrix_a)
inverse_matrix = np.linalg.inv(matrix_a)
determinant = np.linalg.det(matrix_a)
print("Matrix Product:", matrix_product)
print("Inverse:", inverse_matrix)
print("Determinant:", determinant) 

# Random Number Generation
""" random_float = np.random.rand()
print("random_float:",random_float)
rand_ints = np.random.randint(1, 100, (3, 3))
normals = np.random.normal(0, 1, (3, 3))
print("Random Integers:", rand_ints)
print("Normal Distribution:", normals)


empty_array = np.empty((2, 3)) # uninitialized values any random data left in memory
print(empty_array)

array1 = np.arange(10)
print("array1:", array1)

array2 = np.arange(1, 10, 2)
print("array2:",array2)

array1 = np.linspace(0, 5, num=10)
print("array1:",array1)

array1 = np.full((2, 3), 5)
print(array1)

my_list = [1, 2, 3, 4, 5]
arr_from_list = np.asarray(my_list)

print("Array from list:",arr_from_list)

my_list = [1, 2, 3, 4, 5]
arr_from_list = np.array(my_list)

print("Array from list:",arr_from_list)

my_list = np.array([1, 2, 3, 4, 5])
arr_from_list = np.asarray(my_list)

print("Array from list:",arr_from_list)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
c = arr.copy()
arr[0] = 42

print(arr)
print(x)
print(c)

original_array = np.array([1, 2, 3, 4, 5])
copied_array = np.copy(original_array)

print("Original array:",original_array)
print("Copied array:",copied_array)

arr = np.arange(10)
print("Array using arange():", arr)

arr = np.arange(1, 10, 2)
print("Array with start, stop, and step:", arr) """

'''arr = np.array([[1, 2, 3],
                [4, 5, 6]])


arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Flattening the array
flattened_arr = arr.flatten()

print("Original Array:")
print(arr)
print("\nFlattened Array:", flattened_arr)

# Transposing the array 
transposed_arr = np.transpose(arr)

print("Original Array:")
print(arr)
print("\nTransposed Array:")
print(transposed_arr)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print("x=",x)


import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)'''
