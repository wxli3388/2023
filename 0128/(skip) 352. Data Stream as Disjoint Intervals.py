class SummaryRanges:

    def __init__(self):
        self.arr = []

    def addNum(self, value: int) -> None:
        if len(self.arr)==0:
            self.arr.append([value, value])
            return
        l, r = 0, len(self.arr)-1
        while l<=r:
            mid = (l+r)//2
            if self.arr[mid][0]<=value<=self.arr[mid][1]:
                return
            if self.arr[mid][1]<=value:
                l = mid+1
            else:
                r = mid-1
        self.arr.insert(l, [value, value])
        if l!=len(self.arr)-1 and self.arr[l+1][0]==value+1:
            self.arr[l+1][0] = self.arr[l][0]
            self.arr.pop(l)
        if l!=0 and self.arr[l-1][1]==value-1:
            self.arr[l-1][1] = self.arr[l][1]
            self.arr.pop(l)
    def getIntervals(self) -> List[List[int]]:
        return self.arr


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()