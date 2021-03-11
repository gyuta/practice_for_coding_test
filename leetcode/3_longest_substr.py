class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        for i in range(len(s)):
            for j in range(i+1,len(s) + 1):
                substr = s[i:j]
                if isValid(substr):
                    if _max < len(substr):
                        _max = len(substr)
        return _max
            
            
def isValid(string: str) -> bool:
	_list = list(string)
	return not any([ s in _list[i+1:] for (i, s) in enumerate(_list)])

if __name__ == "__main__":
	s = Solution()
	ans = s.lengthOfLongestSubstring(" ")
	print(ans)