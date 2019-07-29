# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:39:07 2019

@author: ZhuangChi

2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

#仔细体会上面的这个链表的定义 就能明白了  它实际上是模拟了类似数组的结构 每个元素包含两部分:val值+指向下一单元的索引
#可以像下面这样使用
#a = ListNode(0) #注意必须要传入一个参数 因为ListNode()这个类的初始化需要一个参数
#b = ListNode(1)
#c = ListNode(2)
#a.next = b
#b.next = c
#a.next.val  输出:1
#a.next.next.val 输出:2

#a = ListNode(0)
#bool(a):True
#bool(a.next):False


class Solution(object):
    def addTwoNumbers(self,l1,l2):
        #输入参数部分 l1 l2分别是两个ListNode 而且里面的顺序已经是逆序了 l1.val:2 l1.next.val:4 l1.next.next.val:3
        if l1.val==0 or l1==None:
            return l2
        if l2.val==0 or l2==None:
            return l1
        
        #carry用于表示进位 一开始为0
        carry = 0
        result = ListNode(0)
        
        while l1!=None and l2!=None:
            result_temp = ListNode(0)
            temp= l1.val+l2.val+carry
            result.next = result
            result.val = temp%10
            result_temp.val = temp%10
            carry = temp//10
            l1 = l1.next
            l2 = l2.next
        
        #此时l1或者l2可能有一个为None 也可能两个都为None
        if l1==None and l2==None:
            return result
        if l1==None and l2!=None:
            while l2!=None:
                temp = l2.val+carry
                result.next = result #感觉这里有问题 在第一次的时候,这里会多出一个0 这样最终结果的第一位(逆序)会多出一个0
                result.val = temp%10
                carry = temp//10
                l2 = l2.next
            return result
        
        if l2==None and l1!=None:
            while l1!=None:
                temp = l1.val+carry
                result.next = result
                result.val = temp%10
                carry = temp//10
                l1 = l1.next        
            return result
        
        
"""
re = ListNode(0)
r = re #r相当于re的拷贝
r.val 输出:0
r.next 输出:None
re.val 输出:0
re.next 输出:None

r.next = ListNode(1)
r.next 输出:<__main__.ListNode at 0x1e9f7db4160>
r.val 输出:0
r = r.next

r.val 输出:1
r.next 输出:None

re.val 输出:0
re.next 输出:<__main__.ListNode at 0x1e9f7db4160>

r.next = ListNode(2)
r.val 输出:1
r.next 输出:<__main__.ListNode at 0x1e9f7db49b0>
r.next.val 输出:2
r.next.next 输出:None

re.val 输出:0 
re.next 输出:<__main__.ListNode at 0x1e9f7db4160>
re.next.val 输出:1
re.next.next 输出:<__main__.ListNode at 0x1e9f7db49b0>
"""
"""
上面这一段不太好理解:我是这么想的
re是ListNode(0)  r=re  那么r和re实际是一个内存区域 所以改变r.next指向ListNode(1) 就相当于改变re.next指向ListNode(1)
但是！ r=r.next 这时候r和re就不再是指向一个东西了 re指向原来的东西 而r则指向了r.next(也就是一个新的ListNode(1))

"""

"""
我终于搞懂上面的这个东西了!
1.re是一个不断增长的链
2.r永远是re的最末一位(链的尾端)
3.在r的尾巴上添加新元素,实际上就是在re的尾巴上添加新元素
4.添加完新元素后  r指向新的尾部节点

"""
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10) #相当于改变re.next为ListNode(s%10) 此时re.val:0 re.next:ListNode(s%10)
            r=r.next #然后r指向一个新的ListNode(s%10) 此时r.val:s%10 r.next:None
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0): #carry要么是0要么是1 不可能是2的
            r.next=ListNode(1) #如果最后carry还是1 说明要在最末尾一位补一个1
        return re.next #最开始的0是不需要的

#执行结果：通过
#执行用时 :60 ms, 在所有 Python 提交中击败了88.05%的用户
#内存消耗 :11.7 MB, 在所有 Python 提交中击败了34.03%的用户
"""



"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        val=l1.val+l2.val
        ansnode=ListNode(val%10)
        ansnode.next=self.addTwoNumbers(l1.next,l2.next)
        
        if val>=10:
            ansnode.next=self.addTwoNumbers(ListNode(1),ansnode.next)
        return ansnode
"""
"""
执行结果：通过
执行用时 :108 ms, 在所有 Python 提交中击败了9.44%的用户
内存消耗 :12.1 MB, 在所有 Python 提交中击败了5.07%的用户
"""

"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        pre=0
        first = ListNode(0)
        curr = first
        while(l1 != None) or (l2 != None):
            if l1==None:
                x=0
            else:
                x=l1.val
                l1=l1.next
            if l2==None:
                y=0
            else:
                y=l2.val
                l2=l2.next
            sum = x+y+pre
            mod = sum%10
            pre = sum//10
            curr.next=ListNode(mod)
            curr=curr.next
        if pre==1:
            curr.next=ListNode(1)
        return first.next
"""
"""
执行结果：通过
执行用时 :68 ms, 在所有 Python 提交中击败了65.65%的用户
内存消耗 :11.9 MB, 在所有 Python 提交中击败了11.21%的用户
"""