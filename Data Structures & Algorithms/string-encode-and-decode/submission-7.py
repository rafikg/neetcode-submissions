import urllib.parse 
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # SEP
        sep = "LENGTH"
        l = " ".join([str(len(x)) for  x in strs]).rstrip()
        s= "".join(strs)
        s_to_encode = s + sep + l
        return urllib.parse.quote(s_to_encode)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sep = "LENGTH"
        # decode s
        decoded_s = urllib.parse.unquote(s)
        s,l = "".join(decoded_s.split(sep)[:-1]), decoded_s.split(sep)[-1]
        l = [int(x) for x in l.split(" ")]
        strs = []
        start = 0
        for i  in range(len(l)-1):
            end= start + l[i]
            strs.append(s[start:end])
            start = end
        strs.append(s[start:])
        return strs
            
            

        
