class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}

        for i in range(len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = 1
            else:
                mapS[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in mapT:
                mapT[t[j]] = 1
            else:
                mapT[t[j]] += 1

        if mapS == mapT:
            return True
        else:
            return False
