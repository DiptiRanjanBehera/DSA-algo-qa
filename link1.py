#l1=[11,8,23,7,25,15]
#l2=[6,33,50,31,46,78,16,34]
#double=[8,23,25]
#without creating result node
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
        
    def double_check(self):
        start=self.headval
        while(start is not None):
            inlist=list2.headval
            while(inlist is not None):
                if(start.dataval*2 == inlist.dataval):
                    print(start.dataval)
                    break
                else:
                    inlist=inlist.nextval
            start=start.nextval
list1=Slinkedlist()
list1.headval=Node(11)
e1=Node(8)
e2=Node(23)
e3=Node(7)
e4=Node(25)
e5=Node(15)

list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5

list2=Slinkedlist()
list2.headval=Node(6)
f1=Node(33)
f2=Node(50)
f3=Node(31)
f4=Node(46)
f5=Node(78)
f6=Node(16)
f7=Node(34)

list2.headval.nextval=f1
f1.nextval=f2
f2.nextval=f3
f3.nextval=f4
f4.nextval=f5
f5.nextval=f6
f6.nextval=f7

print("first list is")
list1.listprint()
print("second list is")
list2.listprint()
print("The list of double is")
list1.double_check()
