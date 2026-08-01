class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count out numbers first

        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        # sort by frequency into buckets
        # [[],[],[]]

        buckets = [[] for i in range(len(nums) + 1)]

        # count -> 7 : 2
        for number, frequency in count.items():
            buckets[frequency].append(number)
        
        # [[],[],[7]]
        output = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                
                if len(output) == k:
                    return output