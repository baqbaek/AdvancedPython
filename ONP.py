def infix_to_onp(expr):
    # define precedence of operators
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    # create empty stack for operators
    op_stack = []
    # create empty list for output
    output = []
    # iterate through each character in the expression
    for char in expr:
        # if character is a number, add it to the output
        if char.isnumeric():
            output.append(char)
        # if character is an operator, pop operators from the stack and add them to the output until an operator with
        # lower precedence is found
        elif char in prec:
            while op_stack and prec[char] <= prec.get(op_stack[-1], 0):
                output.append(op_stack.pop())
            op_stack.append(char)
        # if character is an open parenthesis, add it to the stack
        elif char == "(":
            op_stack.append(char)
        # if character is a close parenthesis, pop operators from the stack and add them to the output until an open
        # parenthesis is found
        elif char == ")":
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()
    # pop remaining operators from the stack and add them to the output
    while op_stack:
        output.append(op_stack.pop())
    # join the output list into a single string
    return "".join(output)


expr = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"
print(infix_to_onp(expr))
