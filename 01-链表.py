class LNode:
    def __init__(self,elem,next_ = None):
        self.elem  =  elem 
        self.next = next_


#################################
a =LNode("a")
b =LNode("b")
c =LNode("c")
d =LNode("d")
a.next = b
b.next = c
c.next = d
head = a 

#################################
# 删除整个链表
head = None


################################
#加入元素
#1 表首端插入
s = LNode("s")
s.next = head.next 
head = s

#2 一般情况的元素插入
s =LNode("s")
# 这里先不管pre如何查到
pre = None 
s.next = pre.next
pre.next = s

################################
#删除元素
#1 删除了表首元素
head = head.next

#2一般情况元素删除
pre.next = pre.next.next 
################################


################################
#扫描，定位和遍历
#1 扫描

# p = head
# while p is None and 还需要继续的其他条件
#     #对p节点里的数据进行操作
#     p = p.next 


#2 按下标定位
p = head  
#i  为需要定位的下标
i = 3
while p is None and i>0:
    i -= 1  
    p = p.next 
#3 按元素定位
p = head
#需要满足pred的条件
# while p is not None and  not pred(p.elem):
#     p = p.next

################################
#链表操作的复杂度
#删除表 O(1)
#判断空表 O(1)
#加入元素
    #1 首端加入元素  O(1)
    #2 尾端加入元素  O(n)
    #3 定位加入元素 O(n) 平均情况和最坏情况

#删除元素
    #1 首都删除元素 O(1)
    #2 尾端删除元素 O(n)
    #3 定位删除元素 O(n) 平均情况和最坏情况
    # 其他删除：通常需要扫描整个表或者其中一部分
################################
#打印所有节点
def get_allnode(node):
    print(node.elem)
    if node.next != None:
        get_allnode(node.next)
    else:
       return

 
#求节点的长度 复杂度为O(n) 如果对这个时间敏感，可以额外维护一个值就是整个表的长度
def get_length(head):
    p,n = head,0
    while p is not None:
        p  = p.next
        n +=1 
    return n

#==============单链表的实现==============

class LinkedListUnderflow(ValueError):
    pass


class  lList:
    def __init__(self) -> None:
        self._head = None

    def is_empty(self):
        #判断是否为空
        return self._head is None

    def prepend(self,elem):
        #表首插入元素
        self._head  = LNode(elem,self._head)

    def pop(self):
        #删除顶端元素
        if self._head is None:
            raise LinkedListUnderflow("in pop") 
        e = self._head.elem 

        self._head = self._head.next
        return e

    def append(self,elem):
        #在表的末尾增加元素
        if self._head  is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next

        p.next = LNode(elem)

    def pop_last(self):
        #删除表末尾的元素
        if self._head is None:
            raise LinkedListUnderflow("in pop_list")

        p = self._head

        if p.next == None:
            e = p.elem
            self._head = None
            return e 

        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        return e


    def find(self,find_elem):
        p = self._head
        while p is not None:
            if p.elem == find_elem :
                return p.elem
            p = p.next

        return None

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem,end='')
            if p.next is not None:
                print(',' , end='')
            p = p.next

        print('')


    def elements(self):
        p  = self._head
        while p is not None:
            yield p.elem
            p = p.next


    def finder(self,pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


#==============单链表的变种==============
#1 优化插入的单链表
#尾部的操作是我们常用操作，但是简单链表从末尾操作负载为 O（ n） 我们可以优化这个地方

class NewList(lList):
    def __init__(self) -> None:
        lList.__init__(self)
        self._rear  = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem=elem,self._head)
            self._rear = self._head

        else:
            self._head = LNode(elem=elem,self._head)
    

    def append(self, elem):
        if self._head is  None:
            self._head = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
    
    def pop_last(self):
        # return super().pop_last()
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")

        p = self._head
        if p.next is None:
            e = p.elem
            self._head =None
            return e

        while p.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        self._rear = p
        return e 



#2 循环单链表
#最后一个节点的指向的不是none指向的是表的第一个节点

class LClist:
    def __init__(self) -> None:
        self._rear = None

    
    def is_empty(self):
        return self._rear is None


    def prepend(self,elem):
        #前端插入
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p

        else:
            p.next = self._rear.next 
            self._rear.next = p

    def append(self,elem):
        #尾端插入
        self.prepend(elem)
        self._rear = self._rear.next


    def pop(self):
        #前端弹出
        if self._rear is None:
            raise LinkedListUnderflow("in pop")

        p = self._rear.next 
        if  self._rear == p:
            self._rear = None
        else:
            self._rear = p.next

        return p.elem

    def printall(self):
        #打印表
        if self.is_empty():
            return
        p = self._rear.next

        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next
    def predpop(self):
        #后团弹出
        if self._rear is None:
            raise LinkedListUnderflow("in predpod")

        p = self._rear.next
        while p.next is not  self._rear:
            p = p.next

        p.next = self._rear.next 

        self._rear = p 

#2 双向链表
class Dnode(LNode):
    #双向链表Node
    def __init__(self, elem, prev=None,next_=None):
        LNode.__init__(self,elem,next_)
        self.prev = prev


class Dlist(NewList):
    def __init__(self) -> None:
        NewList.__init__(self)

    def prepend(self, elem):
        p = Dnode(elem,None,self._head)

        if self._head is None:
            self._rear = p 
        else:
            p.next.prev = p 

        self._head = p


    def append(self,elem):
        p = Dnode(elem,self._rear,None)

        if self._head is None:
            self._head = p 

        else: 
            p.prev.next = p   
        self._rear = p 
 
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        
        e =  self._head.elem 
        self._head = self._head.next 
        if self._head is not None:
            self._head.prev = None
        return e 

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("pop last")

        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is   None:
            self._head = None
        else:
            self._rear.next = None
        return e
    


# 3循环双向链表

class LCDlist(NewList):
    def __init__(self) -> None:
        Dlist.__init__(self)

    def prepend(self, elem):
        p = Dnode(elem,None,self._head)
        if self._head is None:
            p.next = p 
            p.prev = p
            self._rear = p 
        else:

            p.next = self._head
            self._head.prev = p 
            self._rear.next = p 
        self._head = p 

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._head
        self._head = head.next
      
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._rear.next = self._head.next
        self._head = self._head.next
        self._head.prev = self._rear 
        return e 
        
    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop")
        e  = self._rear.elem
        
        self._rear = self._rear.prev
        self._head.prev = self._rear
        self._rear.next = self._head
        return e 

#=============链表的反转==============