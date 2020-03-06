/*
sum_search.c

Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Mar 6 2020
Aidan Whelan
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int fun1(int list[], int k, int list_size); //returns 0 if False, 1 if True

int main()
{
  int sample_list[] = {10,15,3,7};
  int sample_k = 17;
  // List size is calculated outside of the function
  //   If arrays are passed into user-defined functions
  //   only the pointer to the first element is passed
  int sample_list_size = sizeof(sample_list)/sizeof(sample_list[0]);
  int result;

  result = fun1(sample_list,sample_k,sample_list_size);
  printf("Sample Result: %d\n\r", result);

  //Validation test: make it fail.
  int bad_list[] = {2,3,4,5};
  int bad_k = 10;
  int bad_list_size = sizeof(bad_list)/sizeof(bad_list[0]);
  result = fun1(bad_list,bad_k,bad_list_size);
  printf("Bad Result: %d\n\r", result);

  return(0);
}

int fun1(int list[], int k, int list_size)
{
  //size_t list_len = sizeof(list)/sizeof(int);
  for(int i=0; i < list_size; i++)
  {
    for(int j = 0; j < list_size; j++)
    {
      if(i != j)
      {
        if(list[i]+list[j]==k)
        {
          return(1);
        }
      }
    }
  }
  return(0);
}
