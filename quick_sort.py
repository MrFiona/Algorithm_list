#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-21 00:03
# Author  : MrFiona
# File    : quick_sort.py
# Software: PyCharm Community Edition


import time
import random
from collections import deque

start = time.time()
init_num_list = []

for i in xrange(1,101):
    init_num_list.append(random.randint(1,10000))


# todo 快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。
# todo 算法步骤：
# todo 1 从数列中挑出一个元素，称为 “基准”（pivot），
# todo 2 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# todo 3 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
# todo 递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会退出，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。



print

def remove_num(unsort_num_list, left, right):
    key = unsort_num_list[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (unsort_num_list[high] >= key):
            high -= 1
        unsort_num_list[low] = unsort_num_list[high]
        while (low < high) and (unsort_num_list[low] <= key):
            low += 1
        unsort_num_list[high] = unsort_num_list[low]
        unsort_num_list[low] = key

    return low



def quick_sort(num_list, left, right):
    if left >= right:
        return

    final_index = remove_num(num_list, left, right)
    quick_sort(num_list, left, final_index-1)
    quick_sort(num_list, final_index+1, right)

    return num_list


quick_sort(init_num_list, 0, len(init_num_list)-1)

index = 0
for num in init_num_list:
    print '%-4d' % num,
    index += 1
    if index != 0 and index % 50 == 0:
        print

print
print time.time() - start









