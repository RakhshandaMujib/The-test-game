import math

def single_digits_only (list_is):
	'''
	This method checks a list of number for any number that has more than 
	2 digits. If there is any, it splits the digits of the same. 

	Argument: 
	list_is - List. The list of numbers to check.

	Returns:
	list_is - Revised list. 
	'''
	index = 0
	while True:
		if list_is[index] >= 10:
			insert = [int(digit) for digit in str(list_is[index])]
			list_is = list_is[:index] + insert + list_is[index+1:]
		index += 1
		if index >= len(list_is):
			break			
	return list_is

def del_spcl_char(list_is):
	'''
	This method removes specifiec the special characters & spaces from a list.

	Argument:
	list_is - List. The list of charcters we want to work with.

	Returns:
	list_is - Revised list.  
	'''
	illegal_char = {' ', '.', ',', '?', "'", '!'}
	list_is = [char for char in list_is if char not in illegal_char]

	return list_is

def main():

	event = input("What do you want to test?\n")
	lower = event.lower()
	unique_letters = set(lower)
	in_order = sorted(unique_letters, key = lower.find)
	filtered = del_spcl_char(in_order)
	letter_count = {letter : lower.count(letter) for letter in filtered}
	counts_list = [count for count in letter_count.values()]
	counts_list = single_digits_only(counts_list)
	is_100 = False		

	print(f"\nHere is your result:")

	while len(counts_list) != 2:
		back = len(counts_list) - 1 
		temp = []
		for front in range(math.ceil(len(counts_list)/2)):
			if back == front:
				temp.append(counts_list[front])
				break 
			temp.append(counts_list[front] + counts_list[back])
			back -= 1
		counts_list = single_digits_only(temp)[:]
		if len(counts_list) == 3 and (counts_list[0]*100) + (counts_list[1]*10) + counts_list[2] == 100:
			is_100 = True
			break

	if is_100:
		result = 100
	else: 
		result = (counts_list[0]*10)+counts_list[1]

	print(f"\n\tWe are {result}% positive about the above!")

if __name__ == '__main__':
	main()