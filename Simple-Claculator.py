''' Hi everyone.
	My name is Tharun Kumar Reddy.
	Today I'm going to a program for a simple calculator.'''

def addition(a,b) :
	'''Take two inputs a and b.
	   Prints the sum value of the two inputs.'''
	print(a+b)

def subtraction(a,b) :
	'''Take two inputs a and b.
	   Prints the difference value of the two inputs.'''
	print(a-b)

def division(a,b) :
	'''Take two inputs a and b.
	   Prints the division value of the two inputs.'''
	if b == 0 :
		print("The denominator should not be equal to zero.")
		b = int(input("Enter the second value (integers only): "))
	else :
		print(a/b)

def multiplication(a,b):
	'''Take two inputs a and b.
	   Prints the product value of the two inputs.'''
	print(a*b)

# Building program for the calculator
while True :
	operator = int(input('1. Addition\n2. Subtraction\n3. Division\n4. Mutliplication\n5. Exit\nSelect an operator :'))
	if operator in [1,2,3,4] :
		a = int(input("Enter the first value (integers only): "))
		b = int(input("Enter the second value (integers only): "))
		if operator == 1 :
			addition(a,b)
		elif operator == 2 :
			subtraction(a,b)
		elif operator == 3 :
			division(a,b)
		elif operator == 4 :
			multiplication(a,b)

	if operator == 5 :
		print("Have a great day!!")
		break
	if operator > 5 :
		operator = int(input('1.addition\n2.subtraction\n3.division\n4.mutliplication\nPlease select an operator :'))