''' Hi everyone.
	My name is tharun Kumar Reddy.
	Today I'm going to make a simple calculator.'''

# Taking values as input
a = int(input("Enter the first value (integers only): "))
b = int(input("Enter the second value (integers only): "))
op = int(input('1.addition\n2.subtraction\n3.division\n4.mutliplication\nSelect an operator :'))

# Building program for the calculator
if op == 1 :
	print(a+b)
elif op == 2 :
	print(a-b)
elif op == 3 :
	if b== 0 :
		b = int(input("enter valid number in second place(Other than zero) : "))
	print(a/b)
elif op == 4 :
	print(a*b)
else :
	op = int(input('1.addition\n2.subtraction\n3.division\n4.mutliplication\nPlease select an operator :'))