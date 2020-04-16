def main():
	#File chaos.py
        # Python programming - An introduction to Computer Science Lecture 1, Exercise 7
	print ("This program illustrates a chaotic function")
	x = eval(input("Enter first number between 0 and 1: "))
	n = eval(input("Enter second number between 0 and 1:  "))
	for i in range (10):
		x = 3.9 * x * (1 - x)
		n = 3.9 * n * (1 - n)
		print (x , n)
main()

