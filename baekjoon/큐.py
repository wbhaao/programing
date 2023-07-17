import sys
from collections import deque

queue = deque()					
input = sys.stdin.readline
N = int(input())			

for i in range(N):
    cmd = input().split()		
    if "push" == cmd[0]:				
        queue.append(int(cmd[1]))
        
    elif "pop" == cmd[0]:				
        if not queue: 
            print(-1)		
        else: 
            print(queue.popleft())
            
    elif "size" == cmd[0]:				
        print(len(queue))
        
    elif "empty" == cmd[0]:			
        if not queue: 
            print(1)	
        else: 
            print(0)
            
    elif "front" == cmd[0]:	
        if not queue: 
            print(-1)		
        else: 
            print(queue[0])
            
    elif "back" == cmd[0]:				
        if not queue: 
            print(-1)			
        else: 
            print(queue[-1])