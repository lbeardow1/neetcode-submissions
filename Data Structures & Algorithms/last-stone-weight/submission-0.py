class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            stones = sorted(stones, reverse=True)
            print(stones)
            result = abs(stones[0]-stones[1])
            stones.pop(0)
            stones.pop(0)
            stones.insert(0,result)
            print(stones)
        return stones[0]