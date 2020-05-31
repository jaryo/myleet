class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        use = [0 for x in range(len(candidates))]
        re = []
        temp = []

        def dfs(candidates, target):
            for i in range(len(candidates))[::-1]:
                if(target == 0):
                    re.append(temp[:])
                    return
                if(target >= candidates[i] and use[i] == 0):
                    if(i < len(candidates) - 1 and use[i+1] == 0 and candidates[i+1] == candidates[i]):
                        continue
                    else:
                        temp.append(candidates[i])
                        use[i] = 1
                        dfs(candidates[:i+1], target - candidates[i])
                        temp.pop()
                        use[i] = 0
        
        dfs(candidates, target)
        return re