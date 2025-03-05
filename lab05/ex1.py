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
     
     def calculate(self):
         calc = self.peek().split(" ")
         ans = f"{calc[1]} {calc[0]} {calc[2]}"
         return eval(ans)
         
    
def implementStack():


    return 0
"""
Example: CLI
python ex1.py '(+ 1 5)'
6

python ex1.py '(* (+ 1 5) 2)'
12

python ex1.py '(- (* 1 3) (/ 6 (+ 1 2)))'
1


s = Stack()
userInput = str(input("Enter expression: "))
userInputSplit = userInput.split("(")
print(userInputSplit)


for i in userInputSplit:
    print(userInputSplit)

s.push(7)
s.push(userInput)

print(s.peek())"""

s = Stack()
s.push("+ 1 2")
print(type(s.peek()))
print(s.calculate())
