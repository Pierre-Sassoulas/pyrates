walk()
jump_high()
for i in range(5):
	height = get_height()
	if height == 1:
		jump()
	elif height > 1:
		jump_high()
	else:
		walk()
	walk()
	walk()
open_chest()
