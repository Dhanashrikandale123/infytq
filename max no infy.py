# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:08:47 2022
'''Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
 

1. Always num1 should be less than num2

2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied

      a. Sum of the digits of the number is a multiple of 3

      b. Number has only two digits

      c. Number is a multiple of 5

3. Display the maximum element from the list

In case of any invalid data or if the list is empty, display -1.'''
@author: mali-
"""

def sum_of_digits(num):
    sum1=0 
    while(num!=0):
        sum1=sum1+num%10
        num=num//10
    if sum1%3==0:
        return True
    else:
        return False
def find_max(num1,num2):
    max_num=-1
    l1=[]
    if num1<num2:
        for num in range(num1,num2+1):
            if num%5==0 and num>9 and num<100 and sum_of_digits(num)==True:
                l1.append(num)
        if len(l1)>0:
            max_num=max(l1)
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)