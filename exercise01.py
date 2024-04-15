# Decimal to Binary
number = int(float(input('Number: ')))
base = int(float(input('Base: ')))

def decimalTo(num, base, list=[]):
	q = num // base
	r = num % base

	if(r == 10):
		r = 'A'
	elif(r == 11):
		r = 'B'
	elif(r == 12):
		r = 'C'
	elif(r == 13):
		r = 'D'
	elif(r == 14):
		r = 'E'
	elif(r == 15):
		r = 'F'

	list.insert(0, r)

	if(q != 0):
		return decimalTo(q, base, list)
	else:
		string = ''

		for d in list:
			string = string + str(d)

		list.insert(0, string)
		return list

numberList = decimalTo(number, base)

print('Converted Number: ' + numberList[0])
