import string
from pass_gen2 import num_of_digits, password_chars

def main(pass_len, special_chars, num_digits):

	password = ""

	if special_chars:
		sample_set = string.printable[:-6]

	else:
		sample_set = string.printable[:62]

	
	
