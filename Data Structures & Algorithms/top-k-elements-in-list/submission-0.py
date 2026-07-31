class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict (int)
        output = []

        for num in nums:
            count[num] += 1
        
        for i in range (k):
            most_freq = max(count, key=count.get)
            output.append(most_freq)
            del count[most_freq]

        return output