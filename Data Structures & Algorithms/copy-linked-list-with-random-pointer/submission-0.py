class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        old_to_new={}
        curr=head
        while curr:
            old_to_new[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            clone=old_to_new[curr]
            if curr.next:
                clone.next=old_to_new[curr.next]
            else:
                clone.next=None
            if curr.random:
                clone.random=old_to_new[curr.random]
            else:
                clone.random=None
            curr=curr.next
        return old_to_new[head]
        