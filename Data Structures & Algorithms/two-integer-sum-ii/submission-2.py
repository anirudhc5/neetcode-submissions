class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1

        while i < j:
            curr = numbers[i] + numbers[j]
            # print(i, j, curr)
            if curr > target:
                j-=1
                continue
            if curr < target:
                i+=1
                continue
            return [i+1, j+1]


        