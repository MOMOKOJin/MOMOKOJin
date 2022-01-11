#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:53:01 2022

@author: momokosmac
"""

#设计一个输入数字自动转列表的函数，但是现在对于10的转译有困难
# input str ,以，分割 ， 然后转int 
def number_convert2(number_list):
    A = number_list.split(',')
    #print(A)
    B = []
    for a in A :
        b = int(a)
        #print(b)
        B.append(b) 
    return B 


def sort_list_big(list_new):
    """
    list排序算法.降序排列
    :param list_new:列表形参
    :return:
    """
    for r in range(len(list_new) - 1):
        # 作对比
        for i in range(r + 1, len(list_new)):
            # 找更大
            if list_new[r] < list_new[i]:
                # 做交换
                list_new[r], list_new[i] = list_new[i], list_new[r]
    return list_new

# 数列排列方法   
def num_orders(numbers):
    odd = []
    even = []
    for number in numbers :
            if number %2==1:
                odd.append(number)
            else:
                even.append(number)

    sort_list_big(odd)
    even.sort()
    orders = odd + even 
    return orders


lists = input('enter the numbers of houses ： ')   
a=number_convert2(lists)
#print(a)
b= num_orders(a)
print('the final order result is :'+ str(b))

"""

Example:
Input: {1, 2, 3, 5, 4, 7, 10}
Output: {7, 5, 3, 1, 2, 4, 10}
Input: {0, 4, 5, 3, 7, 2, 1}
Output: {7, 5, 3, 1, 0, 2, 4}

"""

