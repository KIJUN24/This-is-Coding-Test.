stack = []

stack.append(5)
stack.append(4)
stack.append(7)
# print(stack)
stack.pop()
stack.append(1)
stack.append(2)
stack.pop()

print(stack[::-1])
print(stack)