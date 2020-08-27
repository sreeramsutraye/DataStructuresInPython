#Creating a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#printing the list
    def Printlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data,end=" -> ")
            cur_node = cur_node.next

#adding elements into the list
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

#adding elements in front of the list
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        new_node.next = cur_node
        self.head = new_node

#inserting elements as per the node preceeding 
    def insert(self,key,data):
        if not key:
            print("not there")
            return
        new_node = Node(data)
        cur_node = self.head
        while cur_node.data != key:
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node

#deleting by data present in the node
    def delete(self,key):
        cur_node = self.head
        if cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
        else:
            while cur_node.next.data != key:
                cur_node = cur_node.next
                if cur_node.next is None:
                    print("Not here")
                    return
            delete_node = cur_node.next
            cur_node.next = delete_node.next
            delete_node = None

#printing the whole list
    def LengthOfList(self):
        cur_node = self.head
        length = 0
        while cur_node:
            cur_node = cur_node.next
            length = length+1
        return (length)

#deleting by the position or index values
    def DeleteByPosition(self,position):
        if llist.LengthOfList() < position+1:
            print("Lesser Position")
            return
        cur_node = self.head
        index = 0
        prev = None
        while index != position:
            prev = cur_node
            cur_node = cur_node.next
            index = index+1
        prev.next = cur_node.next
        cur_node = None

#Swapping nodes
    def SwapNodes(self,node_1,node_2):

        if node_1 == node_2:
            return
        prev_node1 = None
        cur_node1 = self.head

        while cur_node1 and cur_node1.data != node_1:
            prev_node1 = cur_node1
            cur_node1 = cur_node1.next
        
        prev_node2 = None
        cur_node2 = self.head

        while cur_node2 and cur_node2.data != node_2:
            prev_node2 = cur_node2
            cur_node2 = cur_node2.next

        if not prev_node1 or not prev_node2:
            print("NTHG")
        
        if prev_node1:
            prev_node1.next = cur_node2
        else:
            self.head = cur_node2
        if prev_node2:
            prev_node2.next = cur_node1
        else:
            self.head = cur_node1
        
        cur_node2.next, cur_node1.next = cur_node1.next, cur_node2.next

#Reversing the whole list and ************ MOST IMP *******
    def Reverse(self):
        cur_node = self.head
        prev_node = None
        next_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
#            print(str(prev_node.data) + str(cur_node.data)+ str(next_node.data))
        self.head = prev_node       

    def find(self,key):
        cur_node = self.head
        index = 0
        while cur_node and cur_node.data != key:
            cur_node = cur_node.next
            index = index +1
        if cur_node:
            return index
        else:
            return False
    
    def AddElements(self):
        cur_node = self.head
        sum = 0
        while cur_node:
            sum += cur_node.data
            cur_node = cur_node.next
        return sum
    
    def AddStringElements(self):
        cur_node = self.head
        sum = ""
        while cur_node:
            sum += cur_node.data
            cur_node = cur_node.next
        return sum
    def MergetwoSortedLists(self,llist):
        p = self.head
        q = llist.head
        s = None
        new_head = None

        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return llist.Printlist()

    def RemoveDuplicates(self):
        lst = []
        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.data in lst:
                prev_node.next = cur_node.next
                cur_node = None
            else:
                lst.append(cur_node.data)
                prev_node = cur_node
            cur_node = prev_node.next
        return llist1.Printlist()

    def NthToEnd(self,nth):
        cur_node = self.head
        index=0
        while cur_node:
            if cur_node and index>=nth:
                print(cur_node.data)
            index+=1
            cur_node=cur_node.next

    def CountOccurency(self,node_value):
        cur_node=self.head
        no_of_occurency = 0
        while cur_node:
            if cur_node.data == node_value:
                no_of_occurency +=1
            cur_node = cur_node.next
        return no_of_occurency

    def Rotate(self,node_value):
        cur_node = self.head
        first_node = cur_node
        prev_node = None
        while cur_node:
            if cur_node.data == node_value:
                self.head = cur_node
                while cur_node.next:
                    cur_node = cur_node.next
                cur_node.next = first_node
                cur_node = prev_node
                cur_node.next = None
            else:
                prev_node = cur_node
                cur_node = cur_node.next
    def is_palindrome(self):
        strng = ""
        cur_node = self.head
        while cur_node:
            strng += cur_node.data
            cur_node = cur_node.next 
        if strng == strng[::-1]:
            return True
        else:
            return False
    def is_palindrome1(self):
        lst = []
        cur_node = self.head
        while cur_node:
            lst.append(cur_node.data)
            cur_node = cur_node.next
        cur_node = self.head
        while cur_node:
            if cur_node.data == lst.pop():
                cur_node=cur_node.next
            else:
                return False
        if not cur_node:
            return True

    def TailToHead(self):
        cur_node = self.head
        head_node = cur_node
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = None
        self.head = cur_node
        cur_node.next = head_node
    def SumOfTwoLists(self,llist2):
        cur_node1 = self.head
        cur_node2 = llist2.head
        strg1 = ""
        strg2 = ""
        while cur_node1:
            strg1 += str(cur_node1.data)
            cur_node1 = cur_node1.next
        while cur_node2:
            strg2 += str(cur_node2.data)
            cur_node2 = cur_node2.next
        sum = int(strg1) + int (strg2)
        strg3 = str(sum)
        llist3 = LinkedList()
        cur_node = llist3.head
        for i in strg3:
            llist3.append(i)
        print(llist3.Printlist())
            

if __name__ == "__main__":

    llist = LinkedList()
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.append(4)
    llist1.append(2)
    llist1.append(1)
    llist1.append(2)
    llist1.append(1)
    llist1.append(2)
    print(llist1.LengthOfList())
    
