# It was my first solutions with complexity O(n^2), pretty shit result
class Solution1:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        except_list = []
        for index1, value1 in enumerate(nums):
            except_list.append(index1)
            for index2, value2 in enumerate(nums):
                if index2 in except_list:
                    continue
                if value2 == target - value1:
                    return [index1, index2]
        return []

# It was my last solution after watching videos, complexity O(n)
class Solution2:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []