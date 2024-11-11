class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        is_negative = False
        if ((a<0) and (not(b<0))): 
            a *= -1
            is_negative = True
        elif ((not(a<0)) and (b<0)):
            b *= -1
            is_negative = True

        result = 0
        for i in range(b):
            result = self.add(result, a)
        if is_negative == True:
            result *= -1
        return result

    def divide(self, a, b):
        is_negative = False
        if ((a<0) and (not(b<0))): 
            a *= -1
            is_negative = True
        elif ((not(a<0)) and (b<0)):
            b *= -1
            is_negative = True
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if is_negative == True:
            result *= -1
        return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, -3))
    print("Example: division: ", calc.divide(-10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))