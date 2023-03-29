class Node:
    def _init_(self,value):
        self.previous=None
        self.data=value
        self.next=None
        
class DoubleyLinkedList:
    def _init_(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous = new_node
            self.head=new_node
    def deleteFromBegining(self):
        if self.isEmpty():
            print("Empty list can not delete element")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.previous = None
    def deleteFromLast(self):
        if self.isEmpty():
            print("Empty list can not delete element")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None            
    def deleteAtPos(self,pos):
        if self.isEmpty():
            print("Can not delete as Linked list is empty")
        elif pos==1:
            self.deleteFromBegining()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count==pos:
                    break
                temp=temp.next
                count+=1
            if temp is None:
                print("There are less than {} element in the linked list. Can not delete at postion {}".format(pos,pos))
                return
            elif temp.next is None:
                self.deleteFromLast()
                return
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            temp.next=None 
            temp.previous = None
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp=temp.next
            
x=DoubleyLinkedList()
x.insertAtBegining(5)
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("No of nodes before deleting",x.length())
p=int(input("Enter position of value to be deleted"))
x.deleteAtPos(p)
x.printLinkedList()
'''
