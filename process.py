"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""
import tui

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""


# TODO: Your code here

def total_records(records):
    total_num = len(records)
    tui.total_records(total_num)


def record_by_serial_no(records):
    number = tui.serial_number()
    record = records[number - 1]
    return record


def record_by_date(records):
    dates = tui.observation_dates()
    covid_list = []
    for data in records:
        for date in dates:
            if data[1] == date:
                covid_list.append(data)
    return covid_list


def records_by_country(records):
    countries = {}
    for data in records:
        countries[data[3]] = []
    for data in records:
        countries[data[3]].append(data)
    return countries


def records_summary(records):
    countries = records_by_country(records)
    for record in records:
        countries[record[3]] = {"confirmed": 0, "deaths": 0, "recovery": 0}
    for record in records:
        confirmed = countries[record[3]]["confirmed"] + int(record[5])
        deaths = countries[record[3]]["deaths"] + int(record[6])
        recovery = countries[record[3]]["recovery"] + int(record[7])
        countries[record[3]]["confirmed"] = confirmed
        countries[record[3]]["deaths"] = deaths
        countries[record[3]]["recovery"] = recovery
    return countries
