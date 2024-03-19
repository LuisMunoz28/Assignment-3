csv_data_list = []  # Used for format student function 
# testing haha
# Funcction used for menu header [no issues]

# Function prints main menu [no issues]
def print_menu():
    # Dictinary used for main menu items
    main_menu = {
    "L" : "List of Students",
    "A" : "Add Student",
    "E" : "Edit Student",
    "D" : "Delete Student",
    "F" : "Find a Student",
    "G" : "GPA",
    "Q" : "Quit"}

    # List of main menu keys
    main_menu_keys = list(main_menu.keys())

    # Declare main header message and use function for header
    header_txt = ("*** Welcome to Student GPA System ! ***")
    print("************************************************************")
    print(f'{header_txt:^60}')
    print("************************************************************")

    # display list of options for main menu
    for i in range(len((main_menu_keys))):
        print(f"{main_menu_keys[i]} - {main_menu[main_menu_keys[i]]}")


# Function for (A) formatting new students
def format_student(student_info):
    # Receives list of student information
    # Returns CSV formatted string of students info EX: "John Smith,111,9.0"

    # Adds new student info into a list of all student data
    csv_data_list.append(student_info)

    # Sets name for csv file 
    file_csv = "student.csv"

    # opens CSV file and saves data to it and writes
    # Mode r+ for ...............
    with open (file_csv, "r+") as file:
        for student in csv_data_list:
                line = (f'{student[1]},{student[0]},{student[2]}''\n')
                file.write(line)

    # The following is used for the text file
    student_data = (f'{student_info[1]:^20} {student_info[0]:^20} {student_info[2]:^20}'"\r")

    file_text = open("student.txt", "a")
    file_text.writelines(student_data)

    file_text.close()


# Function for header for displaying students [no issues]
def display_std_header():
    print("============================================================\r")
    print(f'{'Student Name':^20} {"Student ID":^20} {"GPA":^20}\r')
    print("============================================================\r")


student_info_list = []
# Function for displaying a single students information [Test later]
def display_student(student_info):
    display_std_header()

    student_info_list.append(student_info)

    for student in student_info_list:
        print(student[0],student[1],student[2])

    # The following is used for the text file
    # student_data = (f'{student_info[0]:^20} {student_info[1]:^20} {student_info[2]:^20}'"\r")

    # print(student_data)


csv_file = "student.csv"
# Function for adding students [not working yet]
def add_student():
    file = open('student.csv', 'r')
    id_list = []
    student_info = []

    new_id = int(input('Enter new ID '))
    for line in file:
        list_line = line.split(',')
        id_list.append(list_line[1])

    if new_id not in id_list:
        print(f'ID:{new_id} can be use')
        student_name = input('Enter the students name: ')
        student_GPA = float(input('Enter the students GPA: '))

        student_info.append(new_id)
        student_info.append(student_name)
        student_info.append(student_GPA)

    else:
        print(f'ID:{new_id} is already in use')

    format_student(student_info)

