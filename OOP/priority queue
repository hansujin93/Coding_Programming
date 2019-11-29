class Node:
    def __init__(self, content=None, priority=0, next=None):
        self.content = content
        self.priority = priority        
        self.next = next


class PriorityQueue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.length = 0
        self.head = None

    def insert(self, content, priority):
        node = Node(content, priority)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            # print('--------', last.priority, priority)
            if last.priority > priority:
                self.head = node
                node.next = last
            else:
                while last.next :
                    if last.next.priority > priority:
                        break
                    last = last.next
                # Append the new node
                node.next = last.next
                last.next = node
        self.length = self.length + 1

    def remove(self):
        content = self.head.content
        self.head = self.head.next
        self.length = self.length - 1
        return content
