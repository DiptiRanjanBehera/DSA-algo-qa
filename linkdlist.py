#MARKS scored by student=89,78,99,76,77,67,99,78,98,90
#insert 78 mark at 8th position
#display mark of students at index number 5 and 7
'''
class Node:
    def _init_(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def _init_(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def insert_node(self,pos_insert,val_insert):
        pos=self.headval
        c=1
        while(pos is not None):
            if(c == pos_insert-1):#doubt
                break
            else:
                c+=1
                pos=pos.nextval
        newnode=Node(val_insert)
        newnode.nextval=pos.nextval
        pos.nextval=newnode
    def view_node(self,pos):
        pos_node=self.headval
        c=1
        while(pos is not None):
            if(c == pos):
                break
            else:
                c+=1
                pos_node=pos_node.nextval
        return (pos_node.dataval)
list1=Slinkedlist()
list1.headval=Node(89)
e1=Node(78)
e2=Node(99)
e3=Node(76)
e4=Node(77)
e5=Node(67)
e6=Node(99)
e7=Node(98)
e8=Node(90)
#linking the list
list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=None
list1.listprint()
n=int(input("Enter the value to be inserted"))
i=int(input("Enter the position"))
list1.insert_node(i,n)
print("After insertion")
list1.listprint()
print("Mark of person at 5th index is",list1.view_node(5))
print("Mark of person at 7th index is",list1.view_node(7))
