class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {')':'(','}':'{',']':'['}
        for ch in s:
            if ch in {"{","[","("}:
                stack.append(ch)
            else:
                if not stack: return False
                if stack[-1] == hmap[ch]:
                    stack.pop()
                else:
                    return False
        
        return not stack