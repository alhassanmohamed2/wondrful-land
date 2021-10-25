
no_of_towns = int(input("Number of Towns\n"))
no_of_water_stations = int(input("Number of water stations\n"))
costs_of_each_town = {}
forward_costs = []
backward_costs = []
selected_costs = []
town_selected_top = []
town_selected_down = []


for i in range(1, no_of_towns+1):
	costs_of_each_town[i] = int(input(f"input cost of town: {i}\n"))


for j in range(1, no_of_water_stations+1):
	forward_costs.append(costs_of_each_town[j])
	
for x in range(no_of_towns, no_of_towns-no_of_water_stations ,-1):
	backward_costs.append(costs_of_each_town[x])


selected_costs.append(costs_of_each_town[1])
selected_costs.append(costs_of_each_town[no_of_towns])
town_selected_top.append(1)
town_selected_down.append(no_of_towns)

for z in range(2,no_of_water_stations):

	if costs_of_each_town[z] < costs_of_each_town[no_of_towns - (z-1)] and (z == town_selected_top[-1] + 1):
		selected_costs.append(costs_of_each_town[z])
		town_selected_top.append(z)

	elif costs_of_each_town[z] > costs_of_each_town[no_of_towns - (z-1)] and ((no_of_towns - (z-1)) == town_selected_down[-1] - 1) :
		selected_costs.append(costs_of_each_town[no_of_towns - (z-1)])
		town_selected_down.append(no_of_towns - (z-1))

	else:
		if z > town_selected_top[-1] + 1 and costs_of_each_town[town_selected_top[-1] + 1] < costs_of_each_town[no_of_towns - (z-1)]:

			selected_costs.append(costs_of_each_town[town_selected_top[-1] + 1])
			town_selected_top.append(town_selected_top[-1] + 1)

		elif no_of_towns - (z-1) < town_selected_down[-1] - 1 and costs_of_each_town[town_selected_down[-1] - 1] < costs_of_each_town[z]:

			selected_costs.append(costs_of_each_town[town_selected_down[-1] - 1] )
			town_selected_down.append(town_selected_down[-1] - 1)

		elif (z == town_selected_top[-1] + 1) or ((no_of_towns - (z-1)) == town_selected_down[-1] - 1):
			if costs_of_each_town[town_selected_top[-1] + 1] < costs_of_each_town[town_selected_down[-1] - 1]:
				selected_costs.append(costs_of_each_town[town_selected_top[-1] + 1])
				town_selected_top.append(town_selected_top[-1] + 1)
			else:
				selected_costs.append(costs_of_each_town[town_selected_down[-1] - 1] )
				town_selected_down.append(town_selected_down[-1] - 1)


		
print(f"Min cost is : {min([sum(forward_costs),sum(backward_costs),sum(selected_costs)])}")





