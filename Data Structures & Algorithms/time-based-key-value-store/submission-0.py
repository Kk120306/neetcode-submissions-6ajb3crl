class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append((value, timestamp))
        else:
            self.table[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.table:
            return ""
        arr = self.table[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r: 
            mid = (l + r) // 2
            val, time = arr[mid]

            if time <= timestamp: 
                res = val
                l = mid + 1
            else :
                r = mid - 1
        
        return res
            
        
