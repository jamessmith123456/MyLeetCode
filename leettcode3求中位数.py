# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:03:31 2019

@author: ZhuangChi
"""

#给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
#请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
#你可以假设 nums1 和 nums2 不会同时为空。
#
#示例 1:
#
#nums1 = [1, 3]
#nums2 = [2]
#
#则中位数是 2.0
#示例 2:
#
#nums1 = [1, 2]
#nums2 = [3, 4]
#
#则中位数是 (2 + 3)/2 = 2.5

"""

执行结果：通过
执行用时 :104 ms, 在所有 Python 提交中击败了63.61%的用户
内存消耗 :11.8 MB, 在所有 Python 提交中击败了35.24%的用户

class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        '''

        #最朴素的思想就是每一次遍历（找出其中的最大值和最小值，然后Allnums删除这两个值）
        #就这样一直循环 最后剩下的两个或者一个数就好求中位数了
        
        #啊，还是要看懂题目， 人家说了 nums1和nums2是两个有序数组 这样只要将他们按序拼接为一个有序数组就可以了！
        #在拼接后的有序数组中查找中位数，就是直接找中间位置的值就行了
        
        # a = [1,1,2,2,3]
        # a[:-1]  [1,1,2,2]
        # a[-1] 3
        #index1 = round((m+n)*0.5)+1 #math.floor()向下取整  向上取整math.ceil() 向0取整int()
        #四舍五入：round()——奇数向远离0取整，偶数去尾取整；或言之：奇数进位，偶数去尾
        #当小数点为5时 向偶数方向取整 比如round(2.5)为2  round(3.5)为4 round(5.5)为6
        #median = Allnums[index1]
            
        #四种情况(不止4种 因为m n的长度也是不确定的)
        #1. ######
                   #####
        #2.         ########
           #####
        #3. #########
               #########
        #4.      #########
           #########
        #不行，这样分情况太复杂了 因为m n的长度是不确定的
        #             #####     还有可能是         #########   还有可能是          #########
                   ##########              ##########                    ######
       
        m = len(nums1)
        n = len(nums2)
        Allnums = []
        
        index_m = 0
        index_n = 0
        while index_m<m and index_n<n:
            if nums1[index_m] < nums2[index_n]:
                Allnums.append(nums1[index_m])
                index_m += 1
            else:
                Allnums.append(nums2[index_n])
                index_n += 1
        
        if index_m<m:
            Allnums += nums1[index_m:]
        if index_n<n:
            Allnums += nums2[index_n:]
                
        if (m+n)%2==0:
            index1 = (m+n)/2-1
            index2 = (m+n)/2
            median = (Allnums[index1]+Allnums[index2])*0.5
        else:
            index1 = int((m+n-1)*0.5)
            median = Allnums[index1]     
            
        return median
"""



"""
执行结果：通过
执行用时 :108 ms, 在所有 Python 提交中击败了51.29%的用户
内存消耗 :11.9 MB, 在所有 Python 提交中击败了24.80%的用户  
class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        nums1.extend(nums2) # 效果和nums1 += nums2是一样的
        nums1.sort()
        if len(nums1)%2==0:
            return((nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2)-1])*0.5)
        else:
            return nums1[int((len(nums1)-1)/2)]
#这里面要注意的是 list的索引必须为整数int类型 而一般的计算出来的都是浮点数float类型 所以要记得int()
"""       


"""
import numpy as np
class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        return np.median(nums1 + nums2)   
"""
   
"""
如果想要复杂度为O(log(m+n)) 则一定要使用二分法
"""