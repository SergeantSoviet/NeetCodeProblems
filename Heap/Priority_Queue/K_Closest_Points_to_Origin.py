class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = []
        distPoints = {}

        for i in range(len(points)):
            distance = math.sqrt((0 - points[i][0])**2 + (0 - points[i][1])**2)
            if distance not in dist:
                dist.append(distance)
            if distance not in distPoints.keys():
                distPoints[distance] = []
            distPoints[distance].append([points[i][0], points[i][1]])
        
        heapq.heapify(dist)
        minHeap = dist

        res = []
        count = 0
        while count < k:
            val = heapq.heappop(minHeap)
            for i in range(len(distPoints[val])):
                res.append(distPoints[val][i])
                count += 1
        
        return res[0:k]