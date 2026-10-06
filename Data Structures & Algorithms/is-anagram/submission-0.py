class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smahp = {}
        tmahp = {}

        for letter in s:
            if letter not in smahp:
                smahp[letter] = 0
            smahp[letter] += 1

        for letter in t:
            if letter not in tmahp:
                tmahp[letter] = 0
            tmahp[letter] += 1
        
        print(smahp)
        print(tmahp)

        if smahp == tmahp:
            return True
        return False