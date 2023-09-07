## 36.Python dictionaries with keys having multiple inputs.
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
		("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)
print('\n')


lat = []
long = []
plc = []
for i in places:
	lat.append(i[0])
	long.append(i[1])
	plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)
