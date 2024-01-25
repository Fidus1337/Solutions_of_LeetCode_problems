class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# It was my first solutions with complexity O(n log n)
class Solution1(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def form_list(our_list: ListNode):
            result_list = []
            while our_list:
                temp_value = our_list.val
                result_list.append(temp_value)
                our_list = our_list.next
            return result_list

        general_result_list = form_list(list1) + form_list(list2)

        if not general_result_list:
            return None

        general_result_list.sort()

        merged_list = ListNode(general_result_list[0])
        current_element = merged_list
        for val in general_result_list[1:]:
            current_element.next = ListNode(val)
            current_element = current_element.next
        return merged_list

# It was second solution after watching videos, complexity O(n)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return dummy.next