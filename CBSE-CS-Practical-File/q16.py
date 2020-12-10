def cls():
    print("\n"*100)
def isempty(q):
    if q==[]:
        return True
    else:
        return False
def enqueue(q,item):
    q.append(item)
    if len(q)==1:
        front=rear=0
    else:
        rear = len(q)-1
def dequeue(q):
    if isempty(q):
        return "UNDERFLOW"
    else:
        item=q.pop(0)
    if len(q)==0:
        front=rear=None
    return item
def peek(q):
    if isempty(q):
        return "UNDERFLOW"
    else:
        front=0
    return q[front]
def display(q):
    if isempty(q):
        print("QUEUE EMPTY!")
    elif len(q)==1:
        print(q[0],"<==front,rear")
    else:
        front=0
        rear=len(q)-1
        print(q[front],"<-front")
        for a in range(1,rear):
            print(q[a])
        print(q[rear],"<-rear")
queue=[]
front=None
while True:
    cls()
    print("QUEUE OPERATIONS")
    print("1. Enqueue ")
    print("2. Dequeue ")
    print("3. Peek ")
    print("4. Display queue ")
    print("5. Exit ")
    ch=int(input("Enter your choice(1-5): "))
    if ch==1:
        item=int(input("Enter item: "))
        enqueue(queue,item)
        input("Press ENTER to continue...")
    elif ch==2:
        item=dequeue(queue)
        if item=="UNDERFLOW":
            print("UNDERFLOW ! Queue is empty ")
        else:
            print("Dequeued item is ",item)
        input("Press ENTER to continue...")
    elif ch==3:
        item=peek(queue)
        if item=="UNDERFLOW":
            print("UNDERFLOW ! Queue is empty ")
        else:
            print("Frontmost item is ",item)
        input("Press ENTER to continue...")
    elif ch==4:
        display(queue)
        input("Press ENTER to continue...")
    elif ch==5:
        break
    else:
        print("invalid choice !")
        input("Press ENTER to continue...")
        
    
    
