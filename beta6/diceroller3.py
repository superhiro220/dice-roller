import dice

while True :
	try :
		stat = int(input("What stat are you rolling? "))
	except NameError :
		print("Not a number.")
		continue
	try :
		dice = dice.d20
	
	print("roll", dice, "total", stat + dice)