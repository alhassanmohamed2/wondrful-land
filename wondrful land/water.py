no_of_towns = int(input("Number of Towns\n"))
no_of_water_stations = int(input("Number of water stations\n"))
costs_of_each_town = {}
chosen_towns = []
each_cost = []
total_cost = 0

for i in range(1,no_of_towns+1):
	costs_of_each_town[i] = int(input(f"input cost of town: {i}\n"))


sorted_costs_of_each_town = list(dict(sorted(costs_of_each_town.items(), key=lambda item: item[1])).items())

for j in range(no_of_water_stations):
	chosen_towns.append(sorted_costs_of_each_town[j][0])
	each_cost.append(sorted_costs_of_each_town[j][1])

total_cost = sum(each_cost)

print(f"Towns Chosen {chosen_towns}")
print(f"Total Cost {total_cost}")