class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower = 0
        upper = 0
        for c in word:
            if 'a'<=c<='z':
                lower+=1
            else:
                upper+=1
        if lower==0 or upper==0 or upper==1 and 'A'<=word[0]<='Z':
            return True
        return False