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
        if temp is None:
            return None
        print("The print linkedlist is:", end=" ")
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
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def search(self, value):
        temp = self.head
        position = 0
        while temp:
            if temp.value == value:
                return position
            position += 1
            temp = temp.next
        return -1
    
    def pop(self):
        curr = self.head
        if curr is None:
            return None
        elif curr.next is None:
            self.pop_first()
        prev = curr
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        self.tail = prev
        return prev

    def get_kth_element(self, k):
        if self.head is None or self.tail is None or k >= self.length:
            return None
        current = self.head
        for _ in range(k):
            current = current.next
        return current
        
    def delete_kth_element(self, k):
        if self.head is None or k > self.length:
            return None
        if k == 1:
            return self.pop_first()
        else:
            prev = self.get_kth_element(k - 2)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def push_first(self, value):
        temp = self.head
        if temp is None:
            return None
        new_node = Node(value)
        new_node.next = temp
        self.head = new_node
        self.length += 1
        return new_node

    def push(self, value):
        temp = self.head
        if temp is None:
            return None
        while temp.next:
            temp = temp.next
        new_node = Node(value)
        temp.next = new_node
        self.tail = new_node
        self.length += 1
        return new_node

    def insert_kth_element(self, value, k):
        temp = self.head
        if temp is None or k > self.length:
            return None
        elif k == 1:
            return self.push_first(value)
        elif k == self.length:
            return self.push(value)
        else:
            prev = self.get_kth_element(k - 2)
            new_node = Node(value)
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1
            return new_node

    def insert_before_element(self, value, element):
        temp = self.head
        if temp is None:
            return None
        elif temp.value == value:
            return self.push_first(value)
        while temp:
            if temp.next.value == element:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                self.length += 1
                return new_node
            temp = temp.next
        

def array_to_linkedlist(arr):
    new_linkedlist = LinkedList(arr[0])
    for value in arr[1:]:
        new_linkedlist.append(value)
    return new_linkedlist
        
new_linkedlist = LinkedList(1)
new_linkedlist.append(2)
new_linkedlist.append(3)
new_linkedlist.append(4)
new_linkedlist.append(5)
new_linkedlist.print_list()
# print("Pop the last element of the linkedlist", new_linkedlist.pop().value)
# print("Remove the element 2nd in the linkedlist", new_linkedlist.delete_kth_element(2).value)
# print("Insert node at first:",new_linkedlist.push_first(0).value)
# print("Insert node at the last", new_linkedlist.push(6).value)
# print("Insert in kth element", new_linkedlist.insert_kth_element(0, 6).value)
print("Insert before the element", new_linkedlist.insert_kth_element(0, 1).value)
new_linkedlist.print_list()
# arr = [1, 2, 3, 4, 5]
# new_linkedlist = array_to_linkedlist(arr)
# new_linkedlist.print_list()
# search_value = 5
# print(f"The search value of {search_value} is {new_linkedlist.search(search_value)}")