class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # h1 = l1 = ListNode(0)
    # if not head or not head.next:
    #     return 
    count , currnode = 0 , head
    while currnode and count < k:
        currnode = currnode.next
        count += 1
    if count < k : return head
    new_head, prev = self.reverse(head, count)
    head.next = self.reverseKGroup(new_head, k)
    return prev

def reverse(self, head, count):
    prev, cur, nxt = None, head, head
    while count > 0:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        count -= 1
    return (cur, prev)