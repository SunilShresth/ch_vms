import mysql.connector
from mysql.connector import Error
from operator import itemgetter

db_conf_dict = {'host':'localhost', 'database':'VMS', 'user':'vms_user', 'password':'Hell0w0rld!', 'auth_plugin':'mysql_native_password'}

def get_record_list():
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        select_record_query = "select id, firstname, lastname, emailid, organization, sent_department, purpose, ch_personnel, checkin, checkout from visitorinfo"
        cursor.execute(select_record_query)
        record_list = cursor.fetchall()

    except mysql.connector.Error as error:
        print("Failed to select from visitorinfo table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return record_list

def get_sort_parameter_index(parameter):
    if parameter == "firstname":
        return 1
    elif parameter == "organization":
        return 4
    elif parameter == "checkin":
        return 8
    else:
        return 0

def get_sorted_record(record_list, parameter_index):
    sorted_record = sorted(record_list, key=itemgetter(parameter_index))
    return sorted_record

# parameter = "checkin"
# parameter_index = get_sort_parameter_index(parameter)
# record_list =  get_record_list()
# sorted_list = get_sorted_record(record_list, parameter_index)

# for item in sorted_list:
#     print(item)
