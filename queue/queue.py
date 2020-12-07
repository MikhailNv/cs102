class Node:
    def __init__(self, contained_object=None, next=None):
        self.contained_object = contained_object
        self.next=next

class MyQueue:
    def __init__(self):
        self.head = None
        
    def clear(self):
        self.__init__()
    
    def add(self, el):
        if self.head is None:
            self.head = Node(el, None)
        else:
            newEl = self.head
            while newEl.next!=None:
                newEl = newEl.next
            newEl.next = Node(el, None)
            
    def remove(self, index):
        if index != 0:
            fd = Node(None, self.head)
            newFd = fd
            l = newFd.next
            index1 = 0
            while l != None:
                if index==index1:
                    newFd.next = l.next
                    l.next = None
                index1+=1
                newFd = l
                l=l.next
        else:
            self.head=self.head.next
            
            
    def queue_list(self):
        arr=[]
        if self.head is not None:
            f = self.head
            arr.append(f.contained_object)
            while f.next != None:
                f = f.next
                arr.append(f.contained_object)
            return arr
    
    def __str__(self):
        if self.head is not None:
            h = self.head
            out = str(h.contained_object) + '\n' 
            while h.next != None:
                h = h.next
                out += str(h.contained_object) + '\n'
            return out
    
        
        
        
class Country:
    def __init__(self, nation, country, count):
        self.__nation = nation
        self.__country = country
        self.__count = count
    @property
    def nation(self):
        return self.__nation
    @property
    def country(self):
        return self.__country 
    @property
    def count(self):
        return self.__count
    def __str__(self):
        return "\nСтрана: {} \nНация: {} \nЖители: {} \n-----------------".format(self.__nation, self.__country, self.__count)
        
               
n1 = MyQueue()
n1.add(1)
n1.add(2)
n1.add(3)
n1.add(4)
n1.remove(0)
print(n1.queue_list())


Russia = Country("Россия", "Россияне", "150000000")
Finland = Country("Финляндия", "Фины", "5000000")
China = Country("Китай", "Китайцы", "1404000000")


newQ = MyQueue()
newQ.add(Russia)
newQ.add(Finland)
newQ.add(China)
print(newQ)

