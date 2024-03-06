class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ls, lt = {}, {}
        for a, b in zip(s, t):
            if (a not in ls) and (b not in lt):
                ls[a] = b
                lt[b] = a         
            elif ls.get(a) != b or lt.get(b) != a:
                return False
            
        return True