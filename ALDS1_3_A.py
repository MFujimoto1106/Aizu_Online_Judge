expression_element = list(input().split())
stack = []

for i in range(len(expression_element)):
    if expression_element[i].isdecimal():
        stack.append(expression_element[i])
    elif expression_element[i] == "+":
        first_value = int(stack.pop())
        second_value = int(stack.pop())
        stack.append(second_value + first_value)
    elif expression_element[i] == "-":
        first_value = int(stack.pop())
        second_value = int(stack.pop())
        stack.append(second_value - first_value)
    elif expression_element[i] == "*":
        first_value = int(stack.pop())
        second_value = int(stack.pop())
        stack.append(second_value * first_value)

output = int(stack.pop())
print(output)
