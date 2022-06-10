import csv
from HashTable import HashTable

# opens and reads csv file
with open('WGUPSPackageFile.csv') as csvfile:
    package_file_csv = csv.reader(csvfile, delimiter=',')

    #  creates new hashtable and initializes lists for trucks
    hash_table = HashTable()
    truck_one_packages = []
    truck_two_packages = []
    truck_three_packages = []

    # insert values from csv into hashtable
    for row in package_file_csv:
        id = row[0]
        street = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        start = ''
        location = ''
        delivery_status = 'At the hub'
        package = [id, location, street, city, state, zip, deadline, weight, note,
                   start, delivery_status]

        # manually sorts packages onto trucks based on notes and inserts into hash table
        if 'EOD' not in package[6]:
            if 'Delayed on flight---will not arrive to depot until 9:05 am' in package[8] or '3365 S 900 W' in package[2]:
                truck_two_packages.append(package)
            elif '3365 S 900 W' in package[2]:
                truck_two_packages.append(package)
            else:
                truck_one_packages.append(package)

        elif ('EOD' in package[6]) and ('none' not in package[8]):
            if 'Wrong address listed' in package[8]:
                truck_three_packages.append(package)
            elif '84103' in package[5]:
                truck_three_packages.append(package)
            else:
                truck_two_packages.append(package)

        elif ('EOD' in package[6]) and ('none' in package[8]):
            if '177 W Price Ave' in package[2] or '2010 W 500 S' in package[2] or '1330 2100 S' in package[2] or \
                    ('3575 W Valley Central Station bus Loop' in package[2]) or ('3148 S 1100 W' in package[2]):
                truck_one_packages.append(package)

            else:
                if ('84103' in package[5]) or ('84111' in package[5]) or ('84117' in package[5]) or ('84119' in package[5]):
                    if '300 State St' in package[2]:
                        truck_three_packages.append(package)
                    else:
                        truck_two_packages.append(package)
                else:
                    truck_three_packages.append(package)

        hash_table.insert(id, package)

    # gets truck one package list - O(1)
    def get_truck_one_packages():
        return truck_one_packages

    # gets truck two packages list - O(1)
    def get_truck_two_packages():
        return truck_two_packages

    # gets truck three package list - O(1)
    def get_truck_three_packages():
        return truck_three_packages

    # gets full hash table - O(1)
    def get_hash_table():
        return hash_table
