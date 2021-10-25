
import time
from random import randint


no_of_towns = 200000
no_of_water_stations = 10000
costs_of_each_town = {}
selected_costs = []
town_selected_top = []
town_selected_down = []

for i in range(1, no_of_towns+1):
	costs_of_each_town[i] = randint(1, 10000)

values_costs = list(costs_of_each_town.values())
forward_costs = values_costs[:no_of_water_stations]
backward_costs = values_costs[-no_of_water_stations:]

selected_costs.append(costs_of_each_town[1])
selected_costs.append(costs_of_each_town[no_of_towns])
town_selected_top.append(1)
town_selected_down.append(no_of_towns)
start_time = time.time()
for z in range(2,no_of_water_stations):
	if costs_of_each_town[town_selected_top[-1] + 1] < costs_of_each_town[town_selected_down[-1] - 1]:
		selected_costs.append(costs_of_each_town[town_selected_top[-1] + 1])
		town_selected_top.append(town_selected_top[-1] + 1)

	elif costs_of_each_town[town_selected_top[-1] + 1] > costs_of_each_town[town_selected_down[-1] - 1]:
		selected_costs.append(costs_of_each_town[town_selected_down[-1] - 1])
		town_selected_down.append(town_selected_down[-1] - 1)

	elif costs_of_each_town[town_selected_top[-1] + 1] == costs_of_each_town[town_selected_down[-1] - 1]:
		if costs_of_each_town[town_selected_top[-1] + 2] < costs_of_each_town[town_selected_down[-1] - 2]:
			selected_costs.append(costs_of_each_town[town_selected_top[-1] + 1])
			town_selected_top.append(town_selected_top[-1] + 1)
		else:
			selected_costs.append(costs_of_each_town[town_selected_down[-1] - 1])
			town_selected_down.append(town_selected_down[-1] - 1)
end_time = time.time()
print(f"Min cost is : {min([sum(forward_costs),sum(backward_costs),sum(selected_costs)])}")
print(f"Time taken is {end_time-start_time}")





        