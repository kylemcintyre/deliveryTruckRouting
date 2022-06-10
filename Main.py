# Kyle McIntyre
# StudentID: 001040250

from ReadCSV import get_hash_table
from Packages import get_total_distance
import datetime


# get user input for package selection
def get_user_selection():

    user_input = int(input("""
Enter 1 to lookup all packages 
Enter 2 to lookup individual packages
Enter 0 to QUIT\n"""))

    return user_input


# get user input for time
def get_user_time():

    try:
        user_time_input = input('Enter time(HH:MM:SS):')
        (hrs0, mins0, secs0) = user_time_input.split(':')
        user_time = datetime.timedelta(hours=int(hrs0), minutes=int(mins0), seconds=int(secs0))
        return user_time

    except ValueError:
        print('Invalid time\n')
        get_user_time()
        return 0


class Main:
    print('\nWGUPS Routing Program\n')

    # print total delivery miles
    print('WGUPS package delivery completed in', "{0:.2f}".format(get_total_distance(), 2), 'miles.\n')

    # get user input to select all, individual packages, or quit
    user_input = get_user_selection()

    while 1 == 1:

        if user_input == 0:
            print('Exiting program')
            exit()

        if user_input < 1 or user_input > 2:
            print("Invalid entry")
            get_user_selection()
            user_input = get_user_selection()

    # if loop to let user make selection or exit program
        if user_input == 1 or user_input == 2:

            while 1 == 1:

                try:
                    # get user input for selection
                    user_time = get_user_time()
                    print('WGUPS Routing Program')
                    break

                except ValueError:
                    print("Invalid time")
                    user_time = get_user_time()

            # get info for all packages using the users time input
            if user_input == 1:
                try:
                    for i in range(1, 41):

                        try:
                            start_time_temp = get_hash_table().search(str(i))[9]
                            delivery_time_temp = get_hash_table().search(str(i))[10]
                            (hrs1, mins1, secs1) = start_time_temp.split(':')
                            (hrs2, mins2, secs2) = delivery_time_temp.split(':')
                            start_time = datetime.timedelta(hours=int(hrs1), minutes=int(mins1), seconds=int(secs1))
                            delivery_time = datetime.timedelta(hours=int(hrs2), minutes=int(mins2), seconds=int(secs2))
                        except ValueError:
                            exit()

                        # check if package is still at the hub
                        if start_time >= user_time:
                            get_hash_table().search(str(i))[10] = 'At the hub'
                            get_hash_table().search(str(i))[9] = start_time_temp
                            print(f'Package ID: {get_hash_table().search(str(i))[0]}', """ """ f'Status: {get_hash_table().search(str(i))[10]}')

                        # check if package is still en route
                        elif start_time <= user_time:
                            if user_time < delivery_time:
                                get_hash_table().search(str(i))[10] = 'En route'
                                get_hash_table().search(str(i))[9] = start_time_temp
                                print(f'Package ID: {get_hash_table().search(str(i))[0]}', """ """ f'Status: {get_hash_table().search(str(i))[10]}')

                            # check if package has been delivered
                            else:
                                get_hash_table().search(str(i))[10] = 'Delivered at ' + delivery_time_temp
                                get_hash_table().search(str(i))[9] = start_time_temp
                                print(f'Package ID: {get_hash_table().search(str(i))[0]}', """ """ f'Status: {get_hash_table().search(str(i))[10]}')
                    break

                # quit program on error
                except IndexError:
                    print(IndexError)
                    quit()
                except ValueError:
                    print('Invalid entry')
                    quit()

            # get info for a specific package using user input
            elif user_input == 2:
                try:
                    user_package_id = input('Enter a Package ID(1-40): \n')
                    start_time_temp = get_hash_table().search(str(user_package_id))[9]
                    delivery_time_temp = get_hash_table().search(str(user_package_id))[10]

                    (hrs, mins, secs) = start_time_temp.split(':')
                    (hrs, mins, secs) = delivery_time_temp.split(':')

                    start_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    delivery_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                    print(
                        f'Package ID: {get_hash_table().search(str(user_package_id))[0]}\n'
                        f'Address: {get_hash_table().search(str(user_package_id))[2]}, '
                        f'{get_hash_table().search(str(user_package_id))[3]}, '
                        f'{get_hash_table().search(str(user_package_id))[4]}, '
                        f'{get_hash_table().search(str(user_package_id))[5]}\n'
                        f'Deadline: {get_hash_table().search(str(user_package_id))[6]}\n'
                        f'Weight: {get_hash_table().search(str(user_package_id))[7]} KILO\n'
                        f'Note: {get_hash_table().search(str(user_package_id))[8]}')

                    # check if the package is still at the hub
                    if start_time >= user_time:

                        get_hash_table().search(str(user_package_id))[10] = 'At the hub'
                        get_hash_table().search(str(user_package_id))[9] = start_time_temp
                        print(f'Status: {get_hash_table().search(str(user_package_id))[10]}')

                    # check if package is still en route
                    elif start_time <= user_time:

                        if user_time < delivery_time:
                            get_hash_table().search(str(user_package_id))[10] = 'En route'
                            get_hash_table().search(str(user_package_id))[9] = start_time_temp
                            print(f'Status: {get_hash_table().search(str(user_package_id))[10]}')

                        # check if package has been delivered
                        else:
                            get_hash_table().search(str(user_package_id))[10] = 'Delivered at ' + delivery_time_temp
                            get_hash_table().search(str(user_package_id))[9] = start_time_temp
                            print(f'Status: {get_hash_table().search(str(user_package_id))[10]}')

                    quit()

                # quit program on error
                except ValueError:
                    print('Invalid entry')
                    exit()

            # quit program on error
            else:
                print('Invalid entry')
                exit()
