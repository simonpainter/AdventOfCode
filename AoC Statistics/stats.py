import re, requests, json
import matplotlib.pyplot as plt

data = {}
plot_data = {}
for year in range(2015,2024):
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

plot_data[2022].pop()

colour = {2015: "#FFC20A",2016: "#994F00",2017: "#E1BE6A",2018: "#E66100",2019: "#1AFF1A",2020: "#1A85FF",2021: "#005AB5",2022: "#FF0000", 2023:"#000000"}
greyscale = {2015: "#eeeeee",2016: "#cccccc",2017: "#aaaaaa",2018: "#888888",2019: "#666666",2020: "#444444",2021: "#222222",2022: "#111111",2023:"#000000"}

line_marker = {2015: ".-",2016: ".-",2017: ".-",2018: ".-",2019: ".-",2020: ".-",2021: ".-",2022: ".-",2023:"*-"}



for year, stars in plot_data.items():
	plt.plot(range(1, len(stars) + 1), stars, line_marker[year], label=year, c=colour[year])
plt.xlabel('Day')
plt.ylabel('Total stars')
plt.legend() 
plt.show()

for year, stars in plot_data.items():
	percentages = []
	for star in stars:
		percentages.append(star/stars[0]*100)
	plt.plot(range(1, len(percentages) + 1), percentages, line_marker[year], label=year, c=colour[year])
plt.xlabel('Day')
plt.ylabel('Total stars expressed as % of day one stars')
plt.legend() 
plt.show()