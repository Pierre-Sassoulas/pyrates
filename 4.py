walk()
for i in range(5):
	direction = read_string()
	if direction == "le":
		left()
	else:
		right()
	walk()
	walk()
open_chest()
