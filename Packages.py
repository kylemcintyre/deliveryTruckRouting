import Distance
import ReadCSV

# create lists for trucks
truck_one_packages = []
truck_two_packages = []
truck_three_packages = []
truck_one_distance = []
truck_two_distance = []
truck_three_distance = []
truck_one_start = ['8:00:00']
truck_two_start = ['9:10:00']
truck_three_start = ['11:00:00']

# truck one
# sets delivery time for packages on truck one - O(n)
for i, value in enumerate(ReadCSV.get_truck_one_packages()):
    ReadCSV.get_truck_one_packages()[i][9] = truck_one_start[0]
    truck_one_packages.append(ReadCSV.get_truck_one_packages()[i])

# compares truck one delivery address to full address list - O(n^2)
for i, k in enumerate(truck_one_packages):
    for j in Distance.get_addresses():
        if k[2] == j[2]:
            truck_one_distance.append(k[0])
            truck_one_packages[i][1] = j[0]

# sort packages on truck one using greedy algorithm
Distance.get_greedy(truck_one_packages, 1, 0)
truck_one_total_distance = 0

# loop through values for truck one with distance functions to get total distance for truck - O(n)
for i in range(len(Distance.get_truck_one_index())):
    try:
        truck_one_total_distance = Distance.get_distances(int(Distance.get_truck_one_index()[i]), int(Distance.get_truck_one_index()[i + 1]), truck_one_total_distance)

        deliver_package_time = Distance.get_truck_time(
            Distance.get_current_distance(int(Distance.get_truck_one_index()[i]), int(Distance.get_truck_one_index()[i + 1])),
            truck_one_start)
        Distance.get_truck_one_list()[i][10] = (str(deliver_package_time))
        ReadCSV.get_hash_table().update(int(Distance.get_truck_one_list()[i][0]), truck_one_packages)
    except IndexError:
        pass

# truck two
# sets delivery time for packages on truck one - O(n)
for i, value in enumerate(ReadCSV.get_truck_two_packages()):
    ReadCSV.get_truck_two_packages()[i][9] = truck_two_start[0]
    truck_two_packages.append(ReadCSV.get_truck_two_packages()[i])

# compares truck two delivery addresses to full address list - O(n^2)
for i, k in enumerate(truck_two_packages):
    for j in Distance.get_addresses():
        if k[2] == j[2]:
            truck_two_distance.append(k[0])
            truck_two_packages[i][1] = j[0]

# sort packages on truck two using greedy algorithm
Distance.get_greedy(truck_two_packages, 2, 0)
truck_two_total_distance = 0

# loop through values on truck two with distance functions to get total distance for truck two - O(n)
for i in range(len(Distance.get_truck_two_index())):
    try:
        truck_two_total_distance = Distance.get_distances(int(Distance.get_truck_two_index()[i]), int(Distance.get_truck_two_index()[i + 1]), truck_two_total_distance)

        deliver_package_time = Distance.get_truck_time(
            Distance.get_current_distance(int(Distance.get_truck_two_index()[i]), int(Distance.get_truck_two_index()[
                                                   i + 1])), truck_two_start)
        Distance.get_truck_two_list()[i][10] = (str(deliver_package_time))
        ReadCSV.get_hash_table().update(int(Distance.get_truck_two_list()[i][0]), truck_two_packages)
    except IndexError:
        pass

# truck three
# set delivery time for packages on truck three - O(n)
for i, value in enumerate(ReadCSV.get_truck_three_packages()):
    ReadCSV.get_truck_three_packages()[i][9] = truck_three_start[0]
    truck_three_packages.append(ReadCSV.get_truck_three_packages()[i])

# compares truck three delivery addresses to full address list - O(n^2)
for i, k in enumerate(truck_three_packages):
    for j in Distance.get_addresses():
        if k[2] == j[2]:
            truck_three_distance.append(k[0])
            truck_three_packages[i][1] = j[0]

# sort packages on truck three using greedy algorithm
Distance.get_greedy(truck_three_packages, 3, 0)
truck_three_total_distance = 0

# loop through values for truck three with distance functions to get total distance for truck three - O(n)
for i in range(len(Distance.get_truck_three_index())):
    try:
        truck_three_total_distance = Distance.get_distances(int(Distance.get_truck_three_index()[i]), int(Distance.get_truck_three_index()[i + 1]), truck_two_total_distance)

        deliver_package_time = Distance.get_truck_time(
            Distance.get_current_distance(int(Distance.get_truck_three_index()[i]), int(Distance.get_truck_three_index()[i + 1])),
            truck_three_start)
        Distance.get_truck_three_list()[i][10] = (str(deliver_package_time))
        ReadCSV.get_hash_table().update(int(Distance.get_truck_three_list()[i][0]), truck_three_packages)
    except IndexError:
        pass


# add all truck distances to get get total distance traveled - O(1)
def get_total_distance():
    return truck_one_total_distance + truck_two_total_distance + truck_three_total_distance
