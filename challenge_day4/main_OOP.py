class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = ""

    def setNum1(self):
        self.num1 = int(input("Choose a number: "))

    def getNum1(self):
        return self.num1

    def setNum2(self):
        self.num2 = int(input("Choose another one: "))

    def getNum2(self):
        return self.num2

    def setOperator(self):
        self.operator = input("Choose an operation: ")

    def getOperator(self):
        return self.operator
    
    def add(self):
        return self.getNum1() + self.getNum2()
    
    def sub(self):
        return self.getNum1() - self.getNum2()
    
    def mul(self):
        return self.getNum1() * self.getNum2()
    
    def div(self):
        if self.getNum2() == 0:
            return "!!!num2 cannot be a 0!!!"
        else: 
            return self.getNum1() / self.getNum2()
    
    def useCalculator(self):
        while True:
            self.setNum1()
            self.setNum2()
            self.setOperator()
            operator = self.getOperator()

            if operator == "exit":
                break
            elif operator == "+":
                print(self.add())
            elif operator == "-":
                print(self.sub())
            elif operator == "*":
                print(self.mul())
            elif operator == "/":
                print(self.div())
            else:
                print("!!!It's the wrong one!!!")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.useCalculator()
        