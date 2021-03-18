class Solution:
    def longestPalindrome(self, s: str) -> str:
      dp = [][]
      # 初期化
      for i in range(len(s)):
        dp[i][i] = True
        if i+1 < len(s) and s[i] == s[i+1]:
          dp[i][i+1] = True
        else:
          dp[i][i+1] = False
      
      i = 1
      j = 1
      start = 2
      while True:
        #更新 dp =
        i += 1
        j += 1
        if j = len(s) - 1:
          i = 1
          j = start
          start += 1
          if start == 1
        

      for j in range(0,len(s)-2):
        for i in range(1,)

      for i in range(1,len(s)-1):
        dp[i-1][i+1] = dp[i][i] and s[i-1] == s[i+1]
        

      

if __name__ == "__main__":
  s = Solution()
  ans = s.longestPalindrome("aaaa")
  print(ans)