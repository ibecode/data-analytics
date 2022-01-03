"""
This module is responsible for setting up and querying the database.
"""
# import tui
import sqlite3
import csv

import tui

"""
Task 22 - 26: Write suitable functions to query the database as follows:

Setup database
Retrieve the names of all (unique) countries in alphabetical order
Retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number.
Retrieve information for the top 5 countries for confirmed cases
Retrieve information for the top 5 countries for death for specific observation dates


The function for setting up the database should do the following:
- Take a list of records as a parameter
- Use the list passed as a parameter value to create and populate a suitable database. You are required to design a
suitable (small) database.
- It is recommended that you complete this function last and start by creating your database using a tool such as
SQL DB Browser. This would allow you to complete the other database functions first.  You can then complete this
function to generate the database via code.

Each function for querying the database should follow the pattern below:
- Take no parameters
- Query the database appropriately. You may use the module 'tui' to retrieve any additional information 
required from the user to complete the querying.
- Return a list of records as retrieved from the database

"""

default_db = ''


# TODO: Your code here
def database_setup(records):
    db_name = input("Enter database name: ")
    try:
        db = sqlite3.connect(f"{db_name}.db")
        cursor = db.cursor()
        sql = """
            BEGIN TRANSACTION;
            CREATE TABLE IF NOT EXISTS "records" ( 
                "id" INTEGER NOT NULL  UNIQUE,
                "observation_date" TEXT NOT NULL,
                "state" TEXT NOT NULL,
                "country" TEXT NOT NULL,
                "update_date" TEXT NOT NULL,
                "confirmed" INTEGER NOT NULL,
                "deaths" INTEGER NOT NULL,
                "recovered" INTEGER NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            COMMIT;
    
            """
        cursor.executescript(sql)

        global default_db
        default_db = db_name

        for record in records:
            sql = "INSERT INTO records " \
                  "(observation_date, state, country, update_date, confirmed, deaths, recovered )" \
                  "VALUES" \
                  "(?, ?, ?, ?, ?, ?, ?)"
            values = [record[1], record[2], record[3], record[4], record[5], record[6], record[7]]
            cursor.execute(sql, values)

        db.commit()
        db.close()
        print("Database creation completed")
    except IOError:
        tui.error("Unable to create database")


def countries_alpha():
    global default_db
    try:
        countries = {}
        if default_db == '':
            tui.error("setup a database")
        else:
            db = sqlite3.connect(f"{default_db}.db")
            cursor = db.cursor()
            sql = "SELECT country FROM records ORDER BY country ASC"
            cursor.execute(sql)
            records = cursor.fetchall()
            db.close()
            return records
    except TypeError:
        tui.error("Unable to connect")


def record_summary():
    id_num = tui.serial_number()
    global default_db
    try:
        if default_db == '':
            tui.error("setup a database")
        else:
            db = sqlite3.connect(f"{default_db}.db")
            cursor = db.cursor()
            sql = f"SELECT confirmed, deaths, recovered FROM records WHERE id={id_num} ORDER BY country ASC"
            cursor.execute(sql)
            records = cursor.fetchall()
            print(f"confirmed cases {records[0][0]}, deaths {records[0][1]}, recovered cases {records[0][2]}")
            db.close()
            return records[0]
    except TypeError:
        tui.error("Unable to connect")


def top_confirmed_cases():
    global default_db
    try:
        if default_db == '':
            tui.error("setup a database")
        else:
            db = sqlite3.connect(f"{default_db}.db")
            cursor = db.cursor()
            sql = "SELECT * FROM records ORDER BY confirmed DESC LIMIT 5"
            cursor.execute(sql)
            records = cursor.fetchall()
            db.close()
            return records
    except TypeError:
        tui.error("Unable to connect")


def top_countries_death_by_dates():
    obs_date = tui.observation_dates()
    global default_db
    try:
        if default_db == '':
            tui.error("setup a database")
        else:
            db = sqlite3.connect(f"{default_db}.db")
            cursor = db.cursor()
            tcdbd = []
            for date in obs_date:
                sql = f"SELECT * FROM records WHERE observation_date=? ORDER BY deaths DESC LIMIT 5"
                values = [date]
                cursor.execute(sql, values)
                records = cursor.fetchall()
                tcdbd.append(records)
            db.close()
            return tcdbd
    except TypeError:
        tui.error("Unable to connect")


