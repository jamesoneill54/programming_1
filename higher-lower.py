i = 0
previous = input() 

while i < 5:
	current = input ()
	if current > previous:
		print "higher"
	elif current < previous: 
		print "lower"
	else:
		print "equal"
	temp = current
	previous = temp
	i = i + 1