import sys
N = int(sys.stdin.readline().strip())
command =""
stack=[]
for i in range(0,N):
    command = sys.stdin.readline().rstrip()
    if("push" in command):
        p_command= command.split()
        stack.append(p_command[-1])
    elif(command=="pop"):
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif(command=="size"):
        print(len(stack))
    elif(command=="top"):
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif(command=="empty"):
        if len(stack)==0:
            print(1)
        else:
            print(0)

