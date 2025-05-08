class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
         count = {}
         for num in arr:
            next_ = num + difference
            if next_ not in count:
                count[next_] = count.get(num, 0) + 1
            else:
                count[next_] = max(count[next_], count.get(num, 0) + 1)
         return max(count.values())
