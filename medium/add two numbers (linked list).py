class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

head = node1

print(head.val)             # 2
print(head.next.val)        # 4
print(head.next.next.val)   # 3



class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        print(l1, l2)




l1 = [2,4,3]
l2 = [5,6,4]



s = Solution()

s.addTwoNumbers(l1,l2)
        