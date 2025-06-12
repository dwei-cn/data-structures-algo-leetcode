class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brutal force: 对于每个item, 看能不能作为start串成一串, 最长能串多长
        # 也可以sort之后再弄,但是time complexity为nlogn
        # 有一种巧妙地算法,叫做寻找start
        # 就是放到set里面,这样做的目的是为了访问的时候复杂度为1, 然后每个item查看能不能当start point
        # 能当start的标准是: 这个数-1不在set里面, 但是这个数+1在set里面
        # 当然你也可以寻找终点,也是一样的道理
        # 然后再以start为起点.用一个小循环寻找长度, 并和res比较长短
        
        if not nums: return 0

        nums_set = set(nums)
        res = 1                   # 起始最小的Longest Consecutive Sequence应该为1

        for i in nums_set:
            if i-1 not in nums_set and i+1 in nums_set:   # 寻找起点
                count = 0
                start = i
                while start in nums_set:
                    start+=1
                    count+=1       # 第一次start自己的时候就是count
                res = max(count, res)
        
        return res

