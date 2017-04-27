import datetime

# format: 2017-01-01
def get_day_diff(starting_date_str, ending_date_str):

	starting_date = datetime.datetime.strptime(starting_date_str, '%Y-%m-%d').date()
	ending_date = datetime.datetime.strptime(ending_date_str, '%Y-%m-%d').date()
	delta = starting_date - ending_date
	day_diff = abs(delta.days)
	# print starting_date
	# print ending_date
	# print day_diff
	return abs(day_diff)


# todo: negative value
def get_week(starting_date_str, ending_date_str):
	day_diff = get_day_diff(starting_date_str, ending_date_str)
	if(day_diff < 0):
		return -1 # error
	else:
		return (day_diff / 7 + 1)
