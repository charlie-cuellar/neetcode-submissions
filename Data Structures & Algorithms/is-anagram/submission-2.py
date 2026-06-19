class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tfreq = {}
        sfreq = {}
        for letter in s:
            if letter not in sfreq:
                sfreq[letter] = 0
            sfreq[letter] += 1
        
        for letter in t:
            if letter not in tfreq:
                tfreq[letter] = 0
            tfreq[letter] += 1
            
        if tfreq.items() == sfreq.items():
            return True
        return False

