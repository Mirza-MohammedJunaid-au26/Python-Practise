# class Solutions:
#     def removeDuplicates(self,nums):
#         j = 1
#         for i in range(1,len(nums)):
#             if nums[i] != nums[i-1]:
#                 nums[j] = nums[i]
#                 j += 1

#         for del_ind in range(i,j-1,-1):
#             del nums[del_ind]

#         return j,nums

        


# nums = list(map(int,input().split(" ")))
# obj = Solutions()
# print(obj.removeDuplicates(nums))
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return numbers[i],numbers[j]

obj = Solution()
print(obj.twoSum([2,7,11,15],9))