class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def print_all(self):
        temp = self.head
        # print(f"The linked list size is {self.length}")
        print("The linked list is ", end="")
        while temp:
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
        return new_node

    def push_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node

    def find_kth_element(self, k):
        if k < 1 or k > self.length:
            return None
        temp = self.head
        for _ in range(k - 1):
            temp = temp.next
        return temp

    def insert_kth_element(self, k, value):
        if k < 1 or k > self.length + 1:
            return None
        if k == 1:
            return self.push_first(value)
        if k == self.length + 1:
            return self.append(value)

        temp = self.find_kth_element(k - 1)
        if temp is None: return None
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return new_node

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pop(self):
        if self.head is None:
            return None
        if self.length == 1:
            return self.pop_first()

        temp = self.head
        while temp.next.next:
            temp = temp.next
        
        removed_node = temp.next
        self.tail = temp
        self.tail.next = None
        self.length -= 1
        return removed_node

    def delete_kth_element(self, k):
        if k < 1 or k > self.length:
            return None
        if k == 1: return self.pop_first()
        if k == self.length: return self.pop()
        
        temp = self.find_kth_element(k - 1)
        if temp is None: return None
        test = temp.next
        temp.next = test.next
        test.next = None
        self.length -= 1
        return test

    def delete_value(self, value):
        temp = self.head
        if temp is None: return None
        elif temp.value == value: return self.pop_first()
        else:
            while temp.next:
                remove_node = temp.next
                if remove_node.value == value:
                    temp.next = temp.next.next
                    remove_node.next = None
                    self.length -= 1
                    if self.tail == remove_node:
                        self.tail = temp
                    return remove_node
                temp = remove_node
            return None

    def insert_before_value(self, value, before_value):
        temp = self.head
        if temp is None: return None
        elif temp.value == before_value: return self.push_first(value)
        else:
            while temp.next:
                if temp.next.value == before_value:
                    new_node = Node(value)
                    new_node.next = temp.next
                    temp.next = new_node
                    self.length += 1
                    return new_node
                temp = temp.next
            return None

def convert_from_array(arr):
    new_linkedlist = LinkedList()
    for value in arr:
        new_linkedlist.append(value)
    return new_linkedlist

new_linkedlist = convert_from_array([0,1,2,3,4,5,6,7])
new_linkedlist.print_all()
# new_linkedlist.push_first(-1)
# print(f"The first popped value is {new_linkedlist.pop_first().value}")
# print(f"The last popped value is {new_linkedlist.pop().value}")
# print(f"The 3rd value in the linkedlist is {new_linkedlist.find_kth_element(3).value}")
# print(f"Insert value in kth element {new_linkedlist.insert_kth_element(2, 20).value}")
# print(f"Remove the 2nd element {getattr(new_linkedlist.delete_kth_element(3), "value", "Not Found")}")
# print(f"Remove the value in the linkedlist {getattr(new_linkedlist.delete_value(3), "value", "Not Found")}")
print(f"Add the value in the linkedlist before the value {getattr(new_linkedlist.insert_before_value(100, 8), "value", "Not Found")}")
new_linkedlist.print_all()