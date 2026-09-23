class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')',
        '{':'}',
        '[':']'
        }

        for i in s:
            if i in d:
                stack.append(i)
            else: 
                if stack == []:
                    return False
                elif d[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        if not stack:                
            return True
        else:
            return False