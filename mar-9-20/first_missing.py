# first_missing.py
#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
#
# Mar 9 2020
# Aidan Whelan

# Example Inputs
input_A = [3,4,-1,1]    #should return 2
input_B = [1,2,0]       #should return 3

# Solution
def first_missing(input):
    input.sort()        #sort values in ascending order
    for i in range(len(input)-1):   #don't evaluate the final int in sequence
        if(input[i] > 0 and input[i+1] != input[i]+1):  #check if positive and next is in sequence
            print(input[i]+1)
            return
    print(input[-1]+1)  #if none missing in sequence, print next in sequence

# Testing
first_missing(input_A)
first_missing(input_B)
