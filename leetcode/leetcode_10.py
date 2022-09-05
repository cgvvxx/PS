# solved: [10] Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# bruteforcing
#
# Medium
# Runtime: 38 ms (79.54%) / Memory Usage: 13.9 MB (79.15%)
# 단순히 itertools의 product를 이용해서 모든 경우의 수를 리스트로 return
# 이 때, map을 이용해서 단순히 한 줄로 return 가능함 (가독성은 떨어지지만..)

from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        return list(map(lambda x:''.join(x), product(*map(lambda x:letters[x], map(int, list(digits))))))
