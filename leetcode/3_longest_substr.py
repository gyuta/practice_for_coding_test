class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for l in reversed(range(1, len(s) + 1)):
            for i in range(0, len(s) + 1 - l):
                substr = s[i:i+l]
                if isValid(substr):
                    print(substr)
                    return l
            
def isValid(string: str) -> bool:
    _list = list(string)
    for (i,s) in enumerate(_list):
        exist = s in _list[i+1:]
        if exist:
            return False
    return True

if __name__ == "__main__":
    s = Solution()
    ans = s.lengthOfLongestSubstring("abcabcbb")
    print(ans)