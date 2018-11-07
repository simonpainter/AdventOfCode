target = 361527
#target = 1024 #31 steps
#target = 12 #3 steps
#target = 23 #2 steps
#target = 10

for layers in range(1,500):
	lastcorner = ((layers*2)-1)**2
	if lastcorner >= target:
		layer = layers
		break
width = ((layer*2)-1)
print(layer-1)
for corner in range(0,4):
	cornerpoint = lastcorner - (corner * (width-1))
	cornerdistance = (cornerpoint-target)
	print(cornerdistance)

print width
