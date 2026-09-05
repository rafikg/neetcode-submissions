class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s={}
        d_t={}
        for x in s:
            if x in d_s:
                d_s[x]+=1
            else:
                d_s[x]=1
        for x in t:
            if x in d_t:
                d_t[x]+=1
            else:
                d_t[x]=1
        # check if the frequency of each character in s is the same in t
        for x in s:
            if x in d_s and x in d_t:
                if d_s[x]!=d_t[x]:
                    return False
            else:
                return False
        for x in t:
            if x in d_s and x in d_t:
                if d_s[x]!=d_t[x]:
                    return False
            else:
                return False
        return True
        



        