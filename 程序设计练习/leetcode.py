class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        num = 0
        largest = 0
        stored = []
        while head < len(s):
            if s[head] in stored:
                stored = stored[stored.index(s[head])+1:]
                stored.append(s[head])
                num = len(stored)
            else:
                stored.append(s[head])
                num += 1
            head += 1
            if num >= largest:
                largest = num
        return largest


s = Solution().lengthOfLongestSubstring("dvdf")
print s
# s = [1,2,3,4,5,5]
# print s.index(1)
