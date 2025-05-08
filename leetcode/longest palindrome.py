class Solution:
    def longestPalindrome(self, s: str) -> int:
        return min(sum(v&~1 for v in Counter(s).values())+1,len(s))
