class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        re = []
        temp = []

        def dfs(candidates, target):
            for i in range(len(candidates))[::-1]:
                if(target == 0):
                    re.append(temp[:])
                    return
                if(target >= candidates[i]):
                    temp.append(candidates[i])
                    dfs(candidates[:i+1], target-candidates[i])
                    temp.pop()
        dfs(candidates, target)
        return re