dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]
print dictionary

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}


print 1
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
	print city

print 2
asia_cities = []			
for countries, cities in locations['Asia'].iteritems():
	city_country = cities[0] + " - " + countries
	asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
	print city