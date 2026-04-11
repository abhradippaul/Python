class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_all(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return new_node

    def pop(self):
        if self.head is None:
            self.length = 0
            return None
        
        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next
        
        prev.next = None
        self.tail = prev
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head and self.tail:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.length += 1
        return new_node

    def pop_first(self):
        temp = self.head

        if self.head is None and self.tail is None: return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or self.length <= index: return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp: temp.value = value

        return temp

    def insert(self, index, value):
        if index < 0 or self.length <= index or self.length == 0: return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length - 1:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return new_node

    def remove(self, index):
        if index < 0 or self.length <= index or self.length == 0: return None
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

new_linkedlist = LinkedList(10)

new_linkedlist.append(20)
new_linkedlist.append(30)
new_linkedlist.append(40)

# print(new_linkedlist.pop().value)
# new_linkedlist.prepend(00)
# print(new_linkedlist.pop_first().value)
# print(new_linkedlist.get(3).value)
# new_linkedlist.set_value(1, 200)
# new_linkedlist.set_value(2, 300)
# new_linkedlist.insert(2, 0)
new_linkedlist.remove(0)

new_linkedlist.print_all()
print(new_linkedlist.length)