import fileinput

for line in fileinput.input():
	line = line[:-1]		# Removes \n
	line = line.split(' ')		# List of the line's words


	output = ''
	for word in line:
		
		if word[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
			word += 'yay '
			output += word

		else:		# word does not begin with vowel

			consonant_sound = ''
			done = False

			word = list(word)
			while not done:
				if word[0] not in ['a', 'e', 'i', 'o', 'u', 'y']:
					consonant_sound += word.pop(0)
				else:
					prefix = ''.join(word)
					done = True

			suffix = consonant_sound + 'ay '

			word = prefix + suffix
			output += word


print(output)



