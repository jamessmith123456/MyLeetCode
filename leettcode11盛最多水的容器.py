# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:28:36 2019

@author: ZhuangChi
"""
"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。


示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49

"""
height = [1,8,6,2,5,4,8,3,7]


"""
下面这种应该是没错的  仅仅是太慢了...
"""
class Solution(object):
    def maxArea(self,height):
        result = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                width = j-i
                heighth = min(height[i],height[j])
                
                if width*heighth>result:
                    result = width*heighth
        
        return result
            
"""
有啥更快的办法呢....头疼...
自己没想出来  参考官方的解题思路
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            b = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            area = b*h
            if maxArea < area:
                maxArea = area
        return maxArea