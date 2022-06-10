import csv
import datetime

# opens and reads distances csv
with open('WGUPSDistances.csv') as csvfile_1:
    distances_file_csv = list(csv.reader(csvfile_1, delimiter=','))

# opens and reads addresses csv
with open('WGUPSDistanceAddresses.csv') as csvfile_2:
    distance_addresses_csv = list(csv.reader(csvfile_2, delimiter=','))

    # returns addresses csv - O(n)
    def get_addresses():
        return distance_addresses_csv

    # returns total distances in distances_file_csv - O(1)
    def get_distances(row, col, total):
        distances = distances_file_csv[row][col]
        if distances == '':
            distances = distances_file_csv[col][row]

        return total + float(distances)

    # returns current distance in distances_file_csv - O(1)
    def get_current_distance(row, col):
        distance = distances_file_csv[row][col]
        if distance == '':
            distance = distances_file_csv[col][row]

        return float(distance)

    # returns current time for truck - O(n)
    def get_truck_time(distance, truck_list):
        new_time = distance / 18  # truck moves at 18 mph
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total


    # create lists for trucks to be used in greedy algorithm
    truck_one = []
    truck_one_index = []
    truck_two = []
    truck_two_index = []
    truck_three = []
    truck_three_index = []

    # greedy algorithm to determine next best location for a truck to visit - O(n^2)
    def get_greedy(_list, number, current_location):
        package_list = _list

        if not len(package_list):
            return package_list

        lowest_value = 100
        location = 0

        # first check if current distance is lower than the lowest value, if it is then update the lowest value and location
        for i in package_list:
            value = int(i[1])
            if get_current_distance(current_location, value) <= lowest_value:
                lowest_value = get_current_distance(current_location, value)
                location = value

        # scan through package list to determine what truck the package is on
        # updates correct truck list and calls greedy again to get next location
        for i in package_list:
            if get_current_distance(current_location, int(i[1])) == lowest_value:
                if number == 1:
                    truck_one.append(i)
                    truck_one_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    current_location = location
                    get_greedy(package_list, 1, current_location)
                elif number == 2:
                    truck_two.append(i)
                    truck_two_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    current_location = location
                    get_greedy(package_list, 2, current_location)
                elif number == 3:
                    truck_three.append(i)
                    truck_three_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    current_location = location
                    get_greedy(package_list, 3, current_location)

    # start each index at 0
    truck_one_index.insert(0, '0')
    truck_two_index.insert(0, '0')
    truck_three_index.insert(0, '0')

    # return truck lists and indexes - O(1)
    def get_truck_one_list():
        return truck_one

    def get_truck_one_index():
        return truck_one_index

    def get_truck_two_list():
        return truck_two

    def get_truck_two_index():
        return truck_two_index

    def get_truck_three_list():
        return truck_three

    def get_truck_three_index():
        return truck_three_index
