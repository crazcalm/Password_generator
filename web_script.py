"""Notes:

The Web interface will send a JSON object with
three entries: {number:X, special: True, digits: y}

Plan:

I need to finish pass_gen2.py first. I forgot to use the 
num_of_digits function!!! 

It is not needed. The string.printable set includes numbers.
That is why i never used it (or noticed that I didn't use it).
I will deleate that function when I get a chance.

I need to take that option out of my web app interface!
"""


import string, random
from pass_gen2 import password_chars

# Need to test!!!
def main(pass_len, special_chars, num_digits):

	password = ""

	if special_chars:
		sample_set = string.printable[:-6]

	else:
		sample_set = string.printable[:62]

	password += random.choice(string.digits)
	
	password = pawword_chars(password, pass_len, sample_set)

	password = "".join(random.sample(password, pass_len))

	return password

if __name__ == "__main__":
	main()
