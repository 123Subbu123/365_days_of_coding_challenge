## 55.Python program to convert time from 12 hour to 24 hour format
import re

def convert_to_24hour(time_str):
	hour, minute, second, am_pm = re.findall('\d+|\w+', time_str)
	hour = int(hour)
	if am_pm == 'PM' and hour != 12:
		hour += 12
	elif am_pm == 'AM' and hour == 12:
		hour = 0
	return f'{hour:02d}:{minute}:{second}'
print(convert_to_24hour('11:21:30 PM'))
print(convert_to_24hour('12:12:20 AM'))
