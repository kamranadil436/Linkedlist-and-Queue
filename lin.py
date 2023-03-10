class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Deleting a node

    def deleteNode(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    def access_element(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                print(current.data)
            count += 1
            current = current.next

    # Print the linked list

    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + ' ')
            temp = temp.next


llist = LinkedList()  # ObjectCreation
print('Currently the LINKED LIST IS EMPTY', llist.printList())

# ADD NODE's CALLING STATEMENTS

print('--------------------------------', )

x = 1
while x <= 10:  # Increase the length of linkedlist here
    custom_input = eval(input('You are entering at the ' + str(x) + ' Node: '))
    llist.insertAtBeginning(custom_input)
    x = x + 1

# DELETE CALLING STATEMENTS

print('--------------------------------')
llist.printList()
delete_node_element = int(input("Enter the node to delete: "))
llist.deleteNode(delete_node_element)
llist.printList()

# ACCESS CALLING STATEMENTS

print('--------------------------------')
item_to_find = eval(input("Enter the NODE's value to access: "))
llist.access_element(item_to_find)
print('--------------------------------')


#In order to run this, use python3.The length of the linkedList is fixed to 10. 
#python3 lin.py