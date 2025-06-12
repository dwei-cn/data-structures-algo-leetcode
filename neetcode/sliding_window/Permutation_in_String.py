from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 思路, 固定窗口size, 算是比较简单了, 每次如果完全match,计数器matches就+=1, 左指针在不再match之前, 计数器就-=1
        # 每次窗口固定了最后, 进行match判断
        s1_counter = Counter(s1)
        temp = Counter()
        matches = 0
        l = 0
        
        # 滑动窗口
        for r in range(len(s2)):
            # r扩展窗口
            if s2[r] in s1_counter:
                temp[s2[r]]+=1
                if temp[s2[r]] == s1_counter[s2[r]]:
                    matches+=1
            
            # l收缩窗口, 如果即将收缩的item造成了匹配度下降, 则matches -= 1
            if r>=len(s1):
                if s2[l] in temp:
                    if temp[s2[l]] == s1_counter[s2[l]]:
                        matches -= 1
                    temp[s2[l]]-=1
                l+=1

            # 检查是否完全匹配
            if matches == len(s1_counter):
                return True

        return False
