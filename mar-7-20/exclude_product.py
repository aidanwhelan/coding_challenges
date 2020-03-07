# exclude_product.py
#
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
#
# Mar 7 2020
# Aidan Whelan

sample_arr_1 = [1,2,3,4,5]
sample_arr_2 = [3,2,1]

def fun1(array):
    result = []
    # First check case of empty input array
    if(len(array)==0):
        return(result)
    # Then iterate over all elements
    for i in range(len(array)):
        # temp initialized to 1 for use in multiplication
        temp = 1
        for j in range(len(array)):
            if(j!=i):
                # Store products in temp
                temp *= array[j]
        result.append(temp)
    return(result)

fun1(sample_arr_1)
fun1(sample_arr_2)

# Validation test: empty array.
bad_array = []
fun1(bad_array)
