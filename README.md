                                EMPLOYEE MANAGEMENT SYSTEM

DESCRIPTION-

    Made using Python file handling and Stack operations based on Lists.

    A command line interface is also made which asks the user to add, display, update, delete, search or exit the program as per the user's choice.

    I have used the process of file handling to read, write and save the data entered by the user in a Comma separated value based file.

    The values added or modified will be stored in a separate CSV file and could be opened afterwards and also could be stored in Local Files.

TO RUN THE PROJECT-

    Run the main.py file which has the CLI.
    The added dataset has 4 values by default which could by modified as per the user's choice.

CONTENTS-

    emp.py: 
        contains the five main functions-

        create() : To add the values in the CSV file
        read() : To print all the values in the dataset file using file handling.
        update() : To modify values in the dataset using the Unique values of Employee ID
        delete() : To delete a specific Employee's data from the Database file.
        search() : To search for a specific Employee using the Employee ID.

    main.py: 
        contains the Command Line Interface
        used iterative and conditional statements

    emp.csv:
        Dataset in the format of Comma Separated Values.
        Could be opened locally using any spreadsheet software.