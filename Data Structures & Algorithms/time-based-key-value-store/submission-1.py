class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.map.get(key):
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        best = -1
        if not self.map.get(key):
            return ""
        
        l, r = 0, len(self.map.get(key)) - 1
        m = 0

        while l <= r:

            m = (l+r) // 2
            
            if (self.map.get(key)[m][1] == timestamp):
                return self.map.get(key)[m][0]
            
            if (timestamp<self.map.get(key)[m][1]):
                r = m - 1
            else:
                best = m
                l = m + 1
        
        return "" if best == -1 else self.map.get(key)[best][0]
