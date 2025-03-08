import sys


class Stack:
     def __init__(self):
         self.items = []


     def isEmpty(self):
         return self.items == []


     def push(self, item):
         self.items.append(item)


     def pop(self):
         return self.items.pop()


     def peek(self):
         return self.items[len(self.items)-1]


     def size(self):
         return len(self.items)
     
def evaluate_expression(expression):


    stack = Stack()
    tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
   
    for token in tokens:
        if token == ')':  #( indicates end of a expression
            args = []
           
            # Pop elements until '(' is encountered
            while stack.peek() not in ('(', None):
                args.append(stack.pop())
            stack.pop()  # Remove '('
           
            # Pop the operator separately
            operator = args.pop()
           
            arg1 = int(args.pop())
            arg2 = int(args.pop())
           
            # Perform the operation using if/elif statements
            if operator in ('+', '-', '*', '/'):
                if operator == '+':
                    result = arg1 + arg2
                elif operator == '-':
                    result = arg1 - arg2
                elif operator == '*':
                    result = arg1 * arg2
                else:
                    result = arg1 // arg2
               
                # Push the result back onto the stack
                stack.push(str(result))
        else:
            # Push numbers, operators, and '(' onto the stack
            stack.push(token)
   
    # The final result should be the last remaining element on the stack
    return int(stack.pop())




if __name__ == "__main__":


    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(result)





