import pymysql

# Connector to SQL by host, user, password, db, charset
conn = pymysql.connect(host="localhost", user="root",
                       password="Algonquin123", db="dataset", charset="utf8")
# cursor for connection
curs = conn.cursor()

# Grab the dataset sql query to load the table
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from user"
curs.execute(sql)
rows = curs.fetchall()
print(rows)
# User selection to choose options 1.Create, 2.Modify, 3.Delete, 4.Exit
# All the options grabbed by user ID
selection = input(
    "Please enter an option:\n(1) Create a new record\n(2) Modify a record\n(3) Delete a records\n(4) Search records\n(5) Exit\nProgramme by Cookhyeong Lee\n: ")
# First condition to create user into the table, the table can be selected by USER ID
if selection == "1":
    no = input("Enter Number: ")
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    region = input("Enter Region: ")
    date = input("Enter Date: ")
    # Format that stored all the data in strings
    save = 'insert into user VALUES (%s, %s, %s, %s, %s)'
    table = (no, id, name, region, date)
    curs.execute(save, table)
    conn.commit()
    print("User has been created!")

# Second condition to update by user information
elif selection == "2":
    id = input('Type your ID to update your info: ')
    # Load and display what if the table is right to update
    sql = "SELECT * FROM user WHERE id = '{}'".format(id)
    curs.execute(sql)
    result = curs.fetchall()
    print(result)
    options = input(
        "What information would you like to update?(id/name/region/date)")
    # Another if statement it provide what particular information the user wants to update
    if options == "id":
        print("Type new ID: ")
        newId = input(":")
        sql = "UPDATE user SET id = '{}' where id = '{}'".format(newId, id)
        curs.execute(sql)
        print(sql)
        conn.commit()
        print("ID has been updated!")
    # When the user wants to update name in the table
    elif options == "name":
        print("Type new Name: ")
        name = input(": ")
        sql = "UPDATE user SET name = '{}' where id = '{}'".format(name, id)
        curs.execute(sql)
        conn.commit()
        print("Name has been updated!")
    # When the user wants to update region in the table
    elif options == "region":
        print("Type new Region: ")
        region = input(": ")
        sql = "UPDATE user SET region = '{}'where id = '{}'".format(region, id)
        curs.execute(sql)
        result = curs.fetchall()
        conn.commit()
        print("Region has been updated!")
    # When the user wants to update date in the table
    elif options == "date":
        print("Type new Date: ")
        date = input(": ")
        sql = "UPDATE user SET date = '{}'where id = '{}'".format(date, id)
        curs.execute(sql)
        result = curs.fetchall()
        conn.commit()
        print("Date has been updated!")
# Third condition to delete table by user ID
elif selection == "3":
    print("Deleting table is only eligible by ID")
    id = input("Select ID to delete: ")
    sql = "DELETE FROM user WHERE id = '{}'".format(id)
    curs.execute(sql)
    conn.commit()
    print("Table has been deleted")
# Fourth condition to search multiple tables by a key word
elif selection == "4":
    print("Search Keyword in the table")
    # Input part to get a key word
    input = input("Type any keyword to search in the table: ")
    # Query to have input parts to get a key word in the existed table
    sql = "SELECT * FROM USER WHERE ID LIKE '%{}%' OR NAME LIKE '%{}%' OR REGION LIKE '%{}%' OR DATE LIKE '%{}%'".format(
        input, input, input, input)
    curs.execute(sql)
    result = curs.fetchall()
    print(result)

# Last condition to turn off the programme
elif selection == "5":
    print('Programme Designed By Cookhyeong Lee!')
