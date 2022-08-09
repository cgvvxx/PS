# solved: [3] Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# sliding-window
#
# Medium
# Runtime: 42 ms (93.7%) / Memory Usage: 13.8 MB (53.5%)
# 오른쪽 포인터(r)을 증가시켜 나가면서 왼쪽 포인터(l)과 같은 문자를 만나면 l을 증가하면서
# 부분문자열의 최대 길이를 저장

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            check = set()
            l, r = 0, 0
            check.add(s[l])
            ans = 1

            while r < len(s)-1:

                r += 1

                if s[r] in check:

                    while 1:

                        check.remove(s[l])
                        l += 1

                        if s[l-1] == s[r]:
                            break

                check.add(s[r])
                ans = max(ans, len(check))

            return ans

        else:
            return 0
