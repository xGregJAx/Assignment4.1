#Gregory Albert
#gja136
#11158762
#CMPT 145 - LO03
#importing stack and queue modules
import TStack

import TQueue
#create TStack and TQueue objects
stack=TStack.create()
queue=TQueue.create()
#opening the cases file
case_file=open('cases.txt')
month=1 #to represent current month
#looping through all lines in the case_file
for line in case_file:
#removing trailing/leading whitespaces and next line characters
    line=line.strip()
#spliting the line by whitespaces
    cases=line.split(' ')
#looping through the resultant list
    for i in cases:
    #checking if its an urgent case
        if i.startswith('URG'):
      #urgent case, pushing to stack
            TStack.push(stack,i)
        else:
      #normal case, pushing to queue
            TQueue.enqueue(queue,i)
#displaying the cases
    print('Month {:d}:'.format(month),end=' ')
#looping while stack is not empty
    while not TStack.is_empty(stack):
    #removing the element at the top, and printing
        i=TStack.pop(stack)
        print(i,end=' ')
#looping while queue is not empty
    while not TQueue.is_empty(queue):
    #removing the element at the front, and printing
        c=TQueue.dequeue(queue)
        print(i,end=' ')
    print()
    month+=1
