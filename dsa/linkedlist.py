# Learning about linkedlist

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        return True
    
    def pop(self):

        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1
        return True

    def pop_first(self):

        if self.length == 0: return True
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp.value
        
    def get(self, index):

        if self.length <= index or index < 0: return None
        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        if self.length <= index or index < 0: return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp = self.get(index - 1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index >= self.length or index < 0: return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # def find_middle_node(self):
    #     slow = self.head
    #     fast = self.head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #     return slow.value

    # def has_loop(self):
    #     slow = self.head
    #     fast = self.head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #         if fast == slow:
    #             return True
    #     return False

    # def kth_node_from_end(self, k):
    #     slow = self.head
    #     fast = self.head
    #     for _ in range(k):
    #         if not fast:
    #             return None
    #         fast = fast.next
        
    #     while fast:
    #         fast = fast.next
    #         slow = slow.next
        
    #     return slow

    # def remove_duplicate(self):
    #     current = self.head
    #     while current:
    #         runner = current
    #         while runner.next:
    #             if current.value == runner.next.value:
    #                 runner.next = runner.next.next
    #             else:
    #                 runner = runner.next
    #         current = current.next

    def kth_node_from_end(self, k):
        slow = self.head
        fast = self.head
        for _ in range(k):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        return slow



new_linkedlist = LinkedList(10)
new_linkedlist.append(20)
new_linkedlist.append(30)
new_linkedlist.append(40)
new_linkedlist.append(50)
new_linkedlist.append(60)
new_linkedlist.append(70)
new_linkedlist.append(80)
# print(f"The poped value is {new_linkedlist.pop()}")
# new_linkedlist.prepend(70)
# new_linkedlist.prepend(60)
# print(f"The poped value is {new_linkedlist.pop_first()}")
# print(f"The value of the position 0 is {new_linkedlist.get(0)}")
# new_linkedlist.insert(6, 200)
# new_linkedlist.set_value(2, 100)
# print(new_linkedlist.remove(2).value)
# new_linkedlist.reverse()
# new_linkedlist.remove_duplicate()
new_linkedlist.print_list()
# print(f"The middle node is {new_linkedlist.find_middle_node()}")
# print(f"The kth node from end is {new_linkedlist.kth_node_from_end(3).value}")
# print(new_linkedlist.has_loop())
# print()
# print(new_linkedlist.length)