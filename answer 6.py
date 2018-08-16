#Implement a stack and queue using lists.
stack=['Sheenam','Apurva','Yashika']
print('Stack:',stack)
stack.append('Aparna')
print('Updated Stack:',stack)
stack.append('Niharika')
print('Updated Stack:',stack)
stack.pop()
print('Updated Stack:',stack)
stack.pop()
print('Updated Stack:',stack)
print()
#Stack is Last In First Out (LIFO) in this element is added to the last of list
# and deletion also starts from the last element of list

queue=['Sheenam','Apurva','Yashika']
print('Queue:',queue)
queue.append('Aparna')
print('Updated Queue:',queue)
queue.append('Niharika')
print('Updated Queue:',queue)
queue.pop(0)
print('Updated Queue:',queue)
queue.pop(0)
print('Updated Queue:',queue)
#Queue is Firts In First Out(FIFO) in this element is added to the last of list
#but deletion starts from the first element of list
