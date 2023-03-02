class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        pre = chars[0]
        count = 0
        left = 0
        for c in chars:
            if c==pre:
                count+=1
            else:
                chars[left] = pre
                left+=1
                if count>1:
                    for i in str(count):
                        chars[left] = i
                        left+=1
                pre = c
                count = 1
        chars[left] = pre
        left+=1
        if count>1:
            for i in str(count):
                chars[left] = i
                left+=1
        return left
        
        