class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        m = {}
        for p in points:
            x1 = p[0]
            y1 = p[1]
            d = (math.sqrt((x1 - 0)**2 + (y1 - 0)**2))
            
            heapq.heappush(res,d)
            if not m.get(d):
                m[d] = []
            m[d].append(p)
            

        res2 = []
        c = 0
        prev = 0
        
        while c < k:
            dis = heapq.heappop(res)
            if (dis == prev):
                continue
            for v in m[dis]:
                res2.append(v)
                c += 1
                if c >= k:
                    break
            prev = dis



        return res2