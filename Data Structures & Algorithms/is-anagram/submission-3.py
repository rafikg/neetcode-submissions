class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        cnt = [0]*26
        base = ord('a')
        for a, b in zip(s,t):
            cnt[ord(a)-base]+=1
            cnt[ord(b)-base]-=1
        return all(v==0 for v in cnt)
        



        