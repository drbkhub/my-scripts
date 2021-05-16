# >>> find_brackets("A * (B + C) and ((X + Y) / 10) + 5")
# ['(B + C)', '((X + Y) / 10)']

def find_brackets(string):
	expressions = []
	
	position = 0
	open_position = 0
	open_bracket_count = 0
	close_bracker_count = 0
	while position < len(string):
		current_char = string[position]

		if open_bracket_count:
			if current_char == "(":
				open_bracket_count += 1
			elif current_char == ")":
				close_bracker_count += 1

			if open_bracket_count == close_bracker_count:
				expressions.append(string[open_position:position+1])
				open_bracket_count = 0
				close_bracker_count = 0

		elif current_char == "(":
			open_position = position
			open_bracket_count += 1 
		
		elif current_char == ")":
			pass

		position += 1

	return expressions

print(find_brackets("A * (B + C) and ((X + Y) / 10) + 5"))
