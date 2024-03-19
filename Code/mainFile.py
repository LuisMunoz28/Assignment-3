# Declars this as the main function
def main():
    # links functions made in function py file
    import functions

    # Message used for starting file
    start = str(input("\nPlease enter the file name to load student information: "))

    if start == "student.txt":

        file_text = open("student.txt", "r+")

        file_text.writelines("============================================================\r")
        file_text.writelines(f'{'Student Name':^20} {"Student ID":^20} {"GPA":^20}\r')
        file_text.writelines("============================================================\r")

        file_text.close()

        print("Students information has been loaded from file")
    else:
        print(f"{start} does not exist - Bye")
        # ***** NEED TO BE ABLE TO STOP CODE HERE *****

    # ***** LOOP FEELS INEFFICENT *****
    repeat_flag = True
    while repeat_flag:

        # main menu display and options
        functions.print_menu()
        main_menu_choice = input(">>> ").upper()
        
        if main_menu_choice == "L": # List  student option

            # put logic for option L
            
            ()

        elif main_menu_choice == "A":  # Add student option
            functions.add_student()

        elif main_menu_choice == "E":
            print('Function for option E is run')
        elif main_menu_choice == "D":
            print('Function for option D is run')
        elif main_menu_choice == "F":
            print('Function for option F is run')
        elif main_menu_choice == "G":
            print('Function for option G is run')
        elif main_menu_choice == "Q":
            repeat_flag = False
        else:
            print('Invalid Input')


    

if __name__ == "__main__":
    main()