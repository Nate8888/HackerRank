
#Completed Brute Force Solution with no outside help.

#Completed the Optimal Approach using Explanation from User "Andrey Kamaev" On stackoverflow.
#He Quotted "In case of Manhattan distance the median gives a solution"
#https://stackoverflow.com/questions/7154978/shortest-distance-travel-common-meeting-point


#Optimal Approach: Find Median x Coordinate & Find Median Y Coordinate

def find_meeting_point(coordinates):
	allx = [each_c[0] for each_c in coordinates]
	ally = [each_c[1] for each_c in coordinates]
	return calculateMedian(allx,ally)

def calculateMedian(all_x_cords,all_y_cords):
	x_median = sorted(all_x_cords)
	y_median = sorted(all_y_cords)
	x_point = x_median[len(x_median)//2]
	y_point = y_median[len(y_median)//2]
	
	return (int(x_point),int(y_point))

""" Solution with Brute Force (Not Optimal)

def find_meeting_point2(coordinates):
	max_coords_tuple = find_grid_xy(coordinates)
	current_least_pair = []
	leastDistance = 999999999
	# dictionaryOfcoords = {}
	for xCord in range(max_coords_tuple[0]+1):
		for yCord in range(max_coords_tuple[1]+1):
			if(xCord == 0 and yCord == 0):
				current_least_pair.append([0,0])
				leastDistance = bruteForce(coordinates,xCord,yCord)
			calculated = bruteForce(coordinates,xCord,yCord)
			if(calculated < leastDistance):
				leastDistance = calculated
				current_least_pair[0] = [xCord,yCord]
	#   dictionaryOfcoords[(xCord,yCord)] = bruteForce(coordinates,xCord,yCord)
	return (current_least_pair[0][0],current_least_pair[0][1])

def bruteForce(coordinates,x,y):
	distance = 0
	for each_cord in coordinates:
		distance += abs(each_cord[0]-x) + abs(each_cord[1]-y)
	return distance
	
def find_grid_xy(coordinates):
	x = 0
	y = 0
	for coord in coordinates:
		if coord[0] > x:
			x = coord[0]
		if coord[1] > y:
			y = coord[1]
	return (x,y)

print(find_meeting_point([ (0,0),    (3,1),    (2,2),    (4,4),    (0,5) ])) """