# solved: [46] Permutations
# https://leetcode.com/problems/permutations/
# bruteforcing
#
# Medium
# Runtime: 69 ms (37.66%) / Memory Usage: 14 MB (84.21%)
# 단순히 itertools의 permutations 이용

from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return list(map(list, permutations(nums)))
        