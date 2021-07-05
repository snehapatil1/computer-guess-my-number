import random

def computer_guess():
	print('Enter Low and High number as per the number that you have thought of:')
	low = int(input("Low: "))
	high = int(input("High: "))
	feedback = ''
	while feedback.lower() != 'c':
		if low == high:
			guess = low
		else:
			guess = random.randint(low, high)
		feedback = input(f'Is {guess} too high(H) or too low(L) or is it correct(C)?  ')
		if feedback.lower() == 'l':
			low = guess + 1
		if feedback.lower() == 'h':
			high = guess - 1

	print(f'Yay! My guess {guess} is correct!')

computer_guess()