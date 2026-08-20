class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        s = s.replace(" ","").translate(str.maketrans("","",string.punctuation)).lower()
        print(s)
        return s == s[::-1]
        