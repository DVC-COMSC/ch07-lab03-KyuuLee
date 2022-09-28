
# ******************************
# Make your Code
# ******************************
# User Values

numbers = []

for i in range(5):
	numbers.append(int(input()))

avg = sum(numbers) / len(numbers)
print (avg)

for i in range(len(numbers)):
	if numbers[i] > avg:
		print ( numbers[i], end=' ')
	# print (numbers[i], end=' ') if numbers[i] > avg else print (end='')

print ()
# newlst = [ v for v in numbers if v > avg]
# print (newlst)
