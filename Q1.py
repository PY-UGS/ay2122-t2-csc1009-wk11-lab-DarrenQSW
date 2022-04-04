class Calculator:

    # Constructor
    # Initializes the attributes
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.result = 0

    # Adds 2 numbers and prints the result in 2 decimal places
    def adder(self):
        self.result = self.input1 + self.input2
        print("Add: {} + {} = {:.2f}".format(self.input1, self.input2, self.result))

    # Subtracts 2 numbers and prints the result in 2 decimal places
    def subtractor(self):
        self.result = self.input1 - self.input2
        print("Subtract: {} - {} = {:.2f}".format(self.input1, self.input2, self.result))

    # Multiplies 2 numbers and prints the result in 2 decimal places
    def multiplier(self):
        self.result = self.input1 * self.input2
        print("Multiply: {} * {} = {:.2f}".format(self.input1, self.input2, self.result))

    # Divides 2 numbers and prints the result in 2 decimal places
    # Checks if input2 is 0, then print an error message
    def divider(self):
        if self.input2 == 0:
            print("Cannot divide by 0!")
        else:
            self.result = self.input1 / self.input2
            print("Divide: {} / {} = {:.2f}".format(self.input1, self.input2, self.result))

    # Clears the attributes to 0
    def clear(self):
        self.input1 = 0
        self.input2 = 0
        self.result = 0

# Ask user for 2 numbers
input1 = float(input("Please enter the first number: "))
input2 = float(input("Please enter the second number: "))
# Create Calculator object
calculator = Calculator(input1, input2)
# Call the functions defined in the class
calculator.adder()
calculator.subtractor()
calculator.multiplier()
calculator.divider()
calculator.clear()