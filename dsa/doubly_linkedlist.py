class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_all(self):
        temp = self.head
        print(f"The length is {self.length}")
        print(f"The linkedlist is",end=" ")
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def print_all_reverse(self):
        temp = self.tail
        print(f"The length is {self.length}")
        print(f"The reversed linkedlist is",end=" ")
        while temp:
            print(temp.value, end=" ")
            temp = temp.prev
        print()

    def push_first(self, value=None):
        if value is None: return None
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
        self.length += 1
        return new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return new_node

    def find_kth_element(self, k):
        temp = self.head
        if k is None or temp is None: return None
        elif k > self.length: return None
        elif temp is None: return None
        for _ in range(0,k-1):
            temp = temp.next
        return temp

    def insert_kth_element(self, value, k):
        temp = self.head
        if temp is None or k is None: return None
        elif k > self.length or k < 1: return None
        elif k == 1: return self.push_first(value)
        else:
            new_node = Node(value) 
            kth_node = self.find_kth_element(k)
            new_node.next = kth_node
            new_node.prev = kth_node.prev
            kth_node.prev.next = new_node
            kth_node.prev = new_node
            self.length += 1
            return new_node

    def find_by_value(self, value=None):
        temp = self.head
        if temp is None or value is None: return None
        elif temp.value == value: return temp
        elif self.tail.value == value: return self.tail
        else:
            while temp:
                if temp.value == value:
                    return temp
                temp = temp.next
            return None

    def insert_before_value(self, value, new_value):
        temp = self.head
        if value is None or new_value is None or temp is None: return None
        node = self.find_by_value(value)
        if node is None: return None
        new_node = Node(new_value)
        new_node.next = node
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node
        self.length += 1
        return new_node

    def pop(self):
        temp = self.tail
        if temp is None: return None
        elif temp.prev is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.tail = temp.prev
            temp.prev.next = None
            temp.prev = None
            self.length -= 1
        return temp

    def pop_first(self):
        temp = self.head
        if temp is None: return None
        elif temp.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def delete_kth_element(self, k=None):
        temp = self.head
        if (temp or k) is None: return None
        elif k > self.length or k < 1: return None
        elif k == 1: return self.pop_first()
        elif k == self.length: return self.pop()
        delete_node = self.find_kth_element(k)
        if delete_node is None: return None
        delete_node.prev.next = delete_node.next 
        delete_node.next.prev = delete_node.prev
        delete_node.next = None
        delete_node.prev = None
        self.length -= 1
        return delete_node

    def delete_before_value(self, value=None):
        temp = self.head
        if temp is None or value is None: return None
        next_of_delete_node = self.find_by_value(value)
        if next_of_delete_node is None: return None
        delete_node = next_of_delete_node.prev
        if next_of_delete_node is temp: return None
        elif delete_node == temp: return self.pop_first()
        delete_node.prev.next = delete_node.next
        delete_node.next.prev = delete_node.prev
        delete_node.next = None
        delete_node.prev = None
        self.length -= 1
        return delete_node

    def reverse_double_linkedlist(self):
        temp = self.head
        if temp is None: return None
        else:
            while temp:
                next = temp.next
                prev = temp.prev
                if next is None:
                    pass

def convert_array_to_linkedlist(arr):
    linkedlist = LinkedList(arr[0])
    for value in arr[1:]:
        linkedlist.append(value)
    return linkedlist

new_linkedlist = convert_array_to_linkedlist([0,1,2,3,4,5,6])
# print(f"Insert element in the 3rd {getattr(new_linkedlist.inserth_kth_element(40,5), "value", "Not Found")}")
# print(f"The 3rd element in the linkedlist is {getattr(new_linkedlist.find_kth_element(3),"value", "Not Found")}")
# print(f"Insert element before and element {getattr(new_linkedlist.insert_before_value(7,60), "value", "Not Found")}")
# print(f"The popped value is {new_linkedlist.pop().value}")
# print(f"The popped first value is {new_linkedlist.pop_first().value}")
# print(f"Delete element in the linkedlist is {getattr(new_linkedlist.delete_kth_element(1),"value", "Not Found")}")
# print(f"Delete element in the linkedlist is {getattr(new_linkedlist.delete_before_value(1),"value", "Not Found")}")
new_linkedlist.print_all()
new_linkedlist.print_all_reverse()
