# sum_search.py
#
# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?
#
# Mar 6 2020
# Aidan Whelan

sample_list = [10,15,3,7]
sample_k = 17

# Go through each index, and evaluate sums with each other single index.
def fun1(list,k):
    for i in range(len(list)):
        for j in range(len(list)):
            if(i != j):
                if(list[i]+list[j]==k):
                    return(True)
    return(False)

fun1(sample_list,sample_k)

# Validation test: make it fail.
bad_list = [2,3,4,5]
bad_k = 10

fun1(bad_list,bad_k)
