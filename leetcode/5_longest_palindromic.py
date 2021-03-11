class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
          return s[0]

        # 2
        count = 0
        ans = ""
        _max = 0
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                count = 2
                l = i-1
                r = i+2
                while True:
                    if l < 0:
                        break
                    if r > len(s) - 1:
                        break
                    if s[l] != s[r]:
                        break
                    count += 2
                    l -= 1
                    r += 1
                if count > _max:
                    ans = s[l+1: r]
                    _max = len(ans)
        for i in range(1, len(s) -1):
            if s[i-1] == s[i+1]:
                count = 3
                l = i-2
                r = i+2
                while True:
                    if l < 0:
                        break
                    if r > len(s) - 1:
                        break
                    if s[l] != s[r]:
                        break
                    count += 2
                    l -= 1
                    r += 1
                if count > _max:
                    ans = s[l+1: r]
                    _max = len(ans)
        return ans

if __name__ == "__main__":
  s = Solution()
  ans = s.longestPalindrome("aaaa")
  print(ans)