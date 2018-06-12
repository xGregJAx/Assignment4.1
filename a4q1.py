#Gregory Albert
#gja136
#11158762
#CMPT 145 - LO03
#importing stack and queue modules
import TStack

import TQueue
#creating TStack and TQueue objects
stk=TStack.create()
que=TQueue.create()
#opening the cases file
case_file=open('Desktop/cases.txt')
month=1 #to represent current month
#looping through all lines in the case_file
for line in case_file:
#removing trailing/leading whitespaces and next line characters
    line=line.strip()
#spliting the line by whitespaces
    cases=line.split(' ')
#looping through the resultant list
    for c in cases:
    #checking if its an urgent case
        if c.startswith('URG'):
      #urgent case, pushing to stack
            TStack.push(stk,c)
        else:
      #normal case, pushing to queue
            TQueue.enqueue(que,c)
#displaying the cases
    print('Month {:d}:'.format(month),end=' ')
#looping while stack is not empty
    while not TStack.is_empty(stk):
    #removing the element at the top, and printing
        c=TStack.pop(stk)
        print(c,end=' ')
#looping while queue is not empty
    while not TQueue.is_empty(que):
    #removing the element at the front, and printing
        c=TQueue.dequeue(que)
        print(c,end=' ')
    print() #blank line
    month+=1 #next month
