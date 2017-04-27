import datetime

# format: 2017-01-01
def get_day_diff(starting_date_str, ending_date_str):

	starting_date = datetime.datetime.strptime(starting_date_str, '%Y-%m-%d').date()

	# special handling of different format of date
	length = len(ending_date_str.split(' '))

	if length <= 3:
		ending_date_str = ending_date_str[:10]
		ending_date = datetime.datetime.strptime(ending_date_str, '%Y-%m-%d').date()
	else:
		char = ending_date_str.split(' ')
		if len(char[0]) > 3:
			ending_date = datetime.datetime.strptime(ending_date_str[:ending_date_str.index('at')-1], '%B %d, %Y').date()
		else: 
			ending_date = datetime.datetime.strptime(ending_date_str[:ending_date_str.index('at')-1], '%b %d, %Y').date()
	# ending_date = datetime.datetime.strptime(ending_date_str, '%Y-%m-%d').date()
	delta = starting_date - ending_date
	day_diff = abs(delta.days)
	# print starting_date
	# print ending_date
	# print day_diff
	return abs(day_diff)

def get_time(time_str):
	# special handling of different format of date
	length = len(time_str.split(' '))
	if length == 1:
		time_str = time_str[:10]
		ending_date = datetime.datetime.strptime(time_str, '%Y-%m-%d').date()
	else:
		char = time_str.split(' ')
		if len(char[0]) > 3:
			ending_date = datetime.datetime.strptime(time_str[:time_str.index('at')-1], '%B %d, %Y').date()
		else: 
			ending_date = datetime.datetime.strptime(time_str[:time_str.index('at')-1], '%b %d, %Y').date()
	return ending_date


# todo: negative value
def get_week(starting_date_str, ending_date_str):
	day_diff = get_day_diff(starting_date_str, ending_date_str)
	if(day_diff < 0):
		return -1 # error
	else:
		return (day_diff / 7 + 1)
