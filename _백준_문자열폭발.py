import sys
from collections import deque
dq = deque("".join(sys.stdin.readline().split()))
target = sys.stdin.readline().strip()
stack = []
while dq:
    stack.append(dq.popleft())
    if len(stack)<len(target):
        continue
    elif "".join(stack[-len(target):]) == target:
        del stack[-len(target):]
if stack:
    print("".join(stack))
else:
    print("FRULA")



