class Solution:
    def appendCharacters(self, s: str, t: str) -> int:



        t_ptr = 0
        for c in s:
            if t_ptr > len(t) - 1:
                break
            if c == t[t_ptr]:
                t_ptr += 1
            
        return len(t) - t_ptr
        
