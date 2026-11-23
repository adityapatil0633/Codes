class Node:
    def __int__(self,data):
        self.data = data
        self.next = Null 
        
    def reverse_linkedlist(head):
     prev = None
     current = head
     while current is not None:
         next_node = current next
         current next = prev
         prev = current
         current = next_node
         return prev 
     def display(head):
        current = head
        while current is not None:
            print(current data)
            current = current.next
            print("Null")
            
             
            
        
         
         