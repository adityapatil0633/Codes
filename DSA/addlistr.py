class listnode:
    def __init__(self,val=0,next=None):
          self.val = val
          self.next = next
    def MergeTwoList(list1 , list2):
        dummy = listNode(-1)
        current= dummy
        while  list1 and list2:
            if list1.val < list2.val:
                current.next=list1
                list = list.next
        else:
            current.next = list2
            List2 = list2.next
            current = current.next
            current.next = List1 or List2
            return dummy.next
        
        
        
        
        
        
        
        