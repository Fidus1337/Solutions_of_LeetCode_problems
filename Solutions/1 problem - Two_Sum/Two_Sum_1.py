# My solution was the best guys, O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        temp_list = []
        temp_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i not in temp_dict:
                temp_list.append(i)
            elif temp_dict[i] in temp_list and temp_list[-1] == temp_dict[i]:
                    temp_list.pop()
            else:
                return False
        return len(temp_list) == 0