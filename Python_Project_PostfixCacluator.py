class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.isEmpty():
            return None and print("Pop from empty stack")
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return None and print("Peek from empty stack")
        else:
            return self.stack[-1]

class Calculator:
    def __init__(self, input_expr):
        self.expr = None
        self.operators = {"^" : 3, "/" : 2, "*" : 2, "+" : 1, "-" : 1}
        self.open = {"(", "{","["}
        self.closed = {")", "}", "]"}
        self.setExpression(input_expr)
    
    #the function that sets the expression and calls the created functions on it 
    def setExpression(self, input_expr):
        self.expr = input_expr.split()
        if len(self.expr) == 0:
            self.setExpression(input("Nothing is not a valid input, please input an expression: "))
        elif self.validateExpression() == False or self.validateParantheses() == False:
            self.setExpression(input("Please input the new or fixed expression: "))
        else:
            self.CalculateExpression()
            print(self.CalculateExpression())
            
    #function to validate numbers
    def isNumber(self, i):
        try:
            float(i)
            return True 
        except:
            return False
    
    #Validates the parantheses
    def validateParantheses(self):
        stack = Stack()
        par_dict = {"(" : ")","[" : "]", "{" : "}"}
        for i in self.expr:
            #checks if open parantheses and pushes it
            if i in self.open:
                stack.push(i)
            #check if closed parantheses
            elif i in self.closed: 
                #invalid parantheses if it has mismatched or missing parantheses
                if stack.isEmpty() or par_dict[stack.pop()] != i:
                    print("Invalid Expression: Mismatched or Missing Parantheses")
                    return False
        #if the stack isn't empty a parantheses is missing from a pair
        if stack.isEmpty():
            return True
        print("Invalid Expression: Missing Parantheses")
        return False
    
    #Validates the expression not including parantheses
    def validateExpression(self):   
        #checks if last or first index is an operator
        if (self.expr[-1] in self.operators or self.expr[0] in self.operators):
            print("Invalid Expression: Last or First Index is an Operator")
            return False
        #a valid expression cannot be this short 
        if len(self.expr) < 3:
            print("Invalid Expression")
            return False 
        
        for i in range(len(self.expr)):
            #checks if index is not a valid charcter
            if (not self.isNumber(self.expr[i]) and 
                self.expr[i] not in self.open and 
                self.expr[i] not in self.closed and 
                self.expr[i] not in self.operators):

                print(f"Invalid Expression: Invalid Character Decected from {self.expr[i]}")
                return False
            
            #for all indexes besides the last one 
            if i < len(self.expr) - 1:
                next = i + 1
                #checks if the next two indexes are operators
                if(self.expr[i] in self.operators and self.expr[next] in self.operators):
                    print(f"Invalid Expression: Two Consecutive Operators from {self.expr[i]} and {self.expr[next]}")    
                    return False
                #checks if the next two indexes are numbers
                elif (self.isNumber(self.expr[i]) and self.isNumber(self.expr[next])):
                    print(f"Invalid Expression: Two Consecutive Numbers from {self.expr[i]} and {self.expr[next]}")
                    return False
                #checks if operator after an open parantheses
                elif self.expr[i] in self.open and self.expr[next] in self.operators:
                    print(f"Invalid Expression: Operator After a Parantheses from {self.expr[i]} and {self.expr[next]}")
                    return False
                #checks if operator before a closed parantheses
                elif self.expr[i] in self.operators and self.expr[next] in self.closed:
                    print(f"Invalid Expression: Operator Before a Parantheses from {self.expr[i]} and {self.expr[next]}")
                    return False
                #divsion by zero error
                elif self.expr[i] == "/" and self.expr[next] == "0":
                    print(f"Invalid Expression: Dividing by Zero at {self.expr[i]} and {self.expr[next]}")
                    return False
        return True

    #Converts the expression from infix to postfix
    def PostFixExpression(self):
        self.implicit_helper()
        stack = Stack()
        postfix = []
        for i in self.expr:
            #checks if a number and casts it 
            if (self.isNumber(i)):
                i = str(float(i))
                postfix.append(i)
            
            #checks if a open parentheses and pushes to stack
            elif (i in self.open):
                stack.push(i)
            
            #checks if an operator
            elif (i in self.operators):
        
                #a special case when the top of the stack and i are both exponentiation, so push to the stack
                if(stack.peek() == "^" and i == "^"):
                    stack.push(i)
                
                #will iterate through the stack, checking these conditons 
                #if it isn't empty, peek isn't an open parantheses and then will pop and append if peek is higher precedence than current operator
                else:
                    while (stack.isEmpty() == False and stack.peek() not in self.open and self.operators[stack.peek()] >= self.operators[i]):
                        postfix.append(stack.pop())
                    stack.push(i)
                
            #checks if closed bracket 
            else:
                #checks if stack isn't empty and top isn't open parentheses, then pops the corresponding open parantheses
                while(stack.isEmpty() == False and stack.peek() not in self.open):
                    #pop and append since it can only be an operator
                    postfix.append(stack.pop())
                stack.pop()
        
        #if there are still indexes left in the stack, pop and append everything out as long as it isn't a parentheses
        while(stack.isEmpty() == False and stack.peek() not in self.closed and stack.peek() not in self.open):
            postfix.append(stack.pop())
        
        
        return postfix
    #Helper function for PostFixExpression that handles implicit multiplcation
    def implicit_helper(self):        
            for i in range(len(self.expr) - 1):
                next = i + 1 

                #Checks if the current index is closed parentheses and the next is a open parentheses then inserts a mutiplication symbol at that index
                if (self.expr[i] in self.closed and self.expr[next] in self.open):
                    self.expr.insert(next, "*")
                
                #if the current index is a number and next is a open parentheses then inserts a mutiplication symbol at that index
                elif (self.isNumber(self.expr[i]) and self.expr[next] in self.open):
                    self.expr.insert(next, "*")

                #if the current index is a closed parentheses and the next index is a number then inserts a mutiplication symbol at that index
                elif (self.expr[i] in self.closed and self.isNumber(self.expr[next])):
                    self.expr.insert(next, "*")
    
    #Calculates the postfix expression using a stack and helper function
    def CalculateExpression(self):
        PostfixExpr = self.PostFixExpression()
        calcStack = Stack()
        result = 0
        for i in PostfixExpr:
            #if a number, will simply push to the stack
            if (self.isNumber(i)):
                calcStack.push(float(i))
            #if a operator, will pop the two most recent numbers and call the helper function
            elif (i in self.operators):
                num1 = calcStack.pop()
                num2 = calcStack.pop()

                result = self.CalculateHelper(num1, num2, i)
                calcStack.push(result)
        
        return calcStack.pop()
    
    #Helper function that calculates the two popped numbers with the correct operator
    def CalculateHelper(self, num1, num2, op):
        sum = 0
        
        if (op == "+"):
            sum += num2 + num1
        
        elif (op == "-"):
            sum += num2 - num1
        
        elif (op == "*"):
            sum += num2 * num1

        elif (op == "/"):
            sum += num2 / num1
        
        elif (op == "^"):
            sum += num2 ** num1

        return sum               

if __name__ == "__main__":
    initial_expression = input("Please input an numerical expression, include spaces to seperate all indexes like ( 1 + 1 ): ")
    calc = Calculator(initial_expression)
    
