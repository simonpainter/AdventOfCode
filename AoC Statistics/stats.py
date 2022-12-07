import re, requests
import matplotlib.pyplot as plt

data = {}
plot_data = {}
for year in range(2015,2023):
	path = "https://adventofcode.com/" + str(year) + "/stats"
	r = requests.get(path)
	stats = re.findall(r'">\s*(\d+)\s*<span class="stats-both">\s*(\d+)\s*<\/span>\s*<span class="stats-firstonly">\s*(\d+)\s*<\/span>',r.text)
	days = {}
	plot_list = []
	for day in stats:
		stars = {'silver': int(day[2]), 'gold': int(day[1]), 'total': int(day[2])+ int(day[1])}
		plot_list.append(int(day[2])+ int(day[1]))
		days[int(day[0])] = stars
	data[year] = days
	plot_list.reverse()
	plot_data[year] = plot_list


for year, stars in plot_data.items():

	plt.plot(range(1, len(stars) + 1), stars, '.-', label=year)
plt.xlabel('Day')
plt.ylabel('Total stars')
plt.legend() 
plt.show()

for year, stars in plot_data.items():
	percentages = []
	for star in stars:
		percentages.append(star/stars[0]*100)
	plt.plot(range(1, len(percentages) + 1), percentages, '.-', label=year)
plt.xlabel('Day')
plt.ylabel('Total stars expressed as % of day one stars')
plt.legend() 
plt.show()