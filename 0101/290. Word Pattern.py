class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(arr)!=len(pattern):
            return False
        pattern_to_s = defaultdict(str)
        s_to_pattern = defaultdict(str)
        for i in range(len(arr)):
            pi = pattern[i]
            si = arr[i]
            if pi not in pattern_to_s and si not in s_to_pattern:
                pattern_to_s[pi] = si
                s_to_pattern[si] = pi
            elif pi not in pattern_to_s or si not in s_to_pattern or pattern_to_s[pi]!=si or s_to_pattern[si]!=pi:
                return False
        return True