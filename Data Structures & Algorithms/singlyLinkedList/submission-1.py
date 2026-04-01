class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        while curr:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next

        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head: 
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0: 
            self.head = self.head.next
            return True


        count = 0
        curr = self.head 

        while curr.next:
            if count + 1 == index:
                curr.next = curr.next.next
                return True
            count += 1
            curr = curr.next
        
        return False
        

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr: 
            values.append(curr.val)
            curr = curr.next

        return values

        
class Node : 

    def __init__(self, val: int):
        self.val = val
        self.next = None