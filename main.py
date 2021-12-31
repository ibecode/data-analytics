"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any database related querying should be done using the appropriate functions the module 'database'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

# Task 10: Import required modules

import tui
import process
import database
import csv

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
covid_records = []


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    # TODO: Your code here
    tui.progress("Data loading operation", 0)
    try:
        with open("./data/covid_19_data.csv") as file:
            csv_read = csv.reader(file)
            heading = next(csv_read)
            for data in csv_read:
                covid_records.append(data)
            record_loaded = len(covid_records)
            tui.total_records(record_loaded)
            tui.progress("Data loading operation", 100)
    except IOError:
        tui.error("Unable to read file")

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        menu_items = tui.menu()

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed. *
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed. *
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.*
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here
        if menu_items == 1:
            sub_menu = tui.menu(menu_items)
            if sub_menu == 1:
                tui.progress("record retrieval process", 0)
                data = process.record_by_serial_no(covid_records)
                print(data)
                tui.progress("record retrieval process", 100)
            elif sub_menu == 2:
                tui.progress("record retrieval process", 0)
                data = process.record_by_date(covid_records)
                print(data)
                tui.progress("record retrieval process", 100)
            elif sub_menu == 3:
                tui.progress("grouping process", 0)
                data = process.records_by_country(covid_records)
                print(data)
                tui.progress("grouping process", 100)
            elif sub_menu == 4:
                tui.progress("summary process", 0)
                data = process.records_summary(covid_records)
                print(data)
                tui.progress("summary process", 100)

        # Task 21: Check if the user selected the option for setting up or querying the database.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has started.
        # - Query the database by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what querying is to be done.
        #   - call the appropriate function in the module 'database' to retrieve the results
        #   - call the appropriate function in the module 'tui' to display the results
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has completed.
        # TODO: Your code here


        # Task 27: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here

        # Task 31: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        # Task 32: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here
        tui.error()



if __name__ == "__main__":
    run()
