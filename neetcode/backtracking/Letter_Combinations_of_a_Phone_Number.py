class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 多维数组的回溯    
        if not digits:
            return []

        keys = {'2':'abc', '3':'def', '4':'ghi', 
                '5':'jkl', '6':'mno', '7':'pqrs', 
                '8':'tuv', '9':'wxyz'}
        arr = [keys[i] for i in digits]

        path = []
        res = []

        def backtrack(ind):
            if len(path) == len(arr):
                res.append(''.join(path[:]))
                return

            for char in arr[ind]:    # 遍历当前层级对应的所有字母
                path.append(char)
                backtrack(ind+1)
                path.pop() 
           
        backtrack(0)
        return res
