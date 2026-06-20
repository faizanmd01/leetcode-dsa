class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # Pehli window ke vowels count karo
        cur = max_v = sum(1 for ch in s[:k] if ch in vowels)
        
        # Window slide karo ek loop mein
        for i in range(k, len(s)):
            cur += (s[i] in vowels) - (s[i - k] in vowels)
            if cur > max_v: max_v = cur
                
        return max_v