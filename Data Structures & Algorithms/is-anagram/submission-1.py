class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # smahp = {}
        # tmahp = {}
        # scount = 0
        # tcount = 0
        # for i, letter in enumerate(s):
        #     smahp[letter] = i
        #     if letter in smahp:
        #         scount += 1
        # for i, letter in enumerate(t):
        #     tmahp[letter] = i
        #     if letter in tmahp:
        #         tcount += 1
        # if smahp.keys() == tmahp.keys() and scount == tcount:
        #     return True
        # return False

        if sorted(s) == sorted(t):
            return True
        return False
        
        # for key, value in smahp.items():
        #     if smahp[key] == tmahp[key]:
        #         return True
        # return False
        
        # failed case
        # s="bbcc"
        # t="ccbc"
        # smahp = {b:0 -> b:1, c:2, - > c:3}
        # scount = 0 -> 1 -> 1 -> 2

        # tmahp = {c: 0 -> c:1, b:2, -> c:3}
        # tcount = 0 -> 1 -> 1 -> 2

