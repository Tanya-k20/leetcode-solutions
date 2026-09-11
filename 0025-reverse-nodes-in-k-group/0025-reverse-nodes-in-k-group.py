# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        arr=[]
        fin=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        
        for i in range(0,len(arr),k):
            group=arr[i:i+k]
            fin.extend(group[::-1] if len(group)==k else group)
        dummy =ListNode(0)
        current=dummy
        for value in fin:
            current.next=ListNode(value)
            current=current.next
        return dummy.next
           
        

        