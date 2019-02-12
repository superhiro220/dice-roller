from random import randint

while True :
	try :
		stat = int(input("What stat are you rolling? "))
	except NameError :
		print("Not a number.")
		continue
	try :
		dice = int(input("What die shall you cast? "))
	except NameError :
		print("Not a number.")
		continue
	roll = randint(1,dice)
	print("roll", roll, "total", stat + roll)