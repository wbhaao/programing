stack_size = 5
lst = [None] * stack_size
top = -1

def isEmpty():
    if top == -1:
        return True
    else:
        return False
def isFull():
    if top == stack_size-1:
        return True
    else:
        return False
def push(e):
    global top
    if isFull():
        print("풀입니당")
    else:
        top += 1
        lst[top] = e
        
def pop():
    global top
    if isEmpty():
        print("엠티입니당")
    else:
        lst[top] = None
        top -= 1
        
def peak():
    if not isEmpty():
        return lst[top]
    else: pass

push(1)
push(1)
push(1)
push(1)
push(1)
push(1)
pop()
pop()
pop()
pop()
pop()
pop()
print(isEmpty())
print(lst)
