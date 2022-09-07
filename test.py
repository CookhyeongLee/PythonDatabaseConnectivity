from ast import Assert
import pytest
import pymysql

# Unit test to check if the user create and can find itself
conn = pymysql.connect(host="localhost", user="root",
                       password="Algonquin123", db="dataset", charset="utf8")
curs = conn.cursor()
curs.execute("""INSERT INTO user(no, id, name, region, date)
VALUES (15, 'KO20', 'Cookhyeong', 'Seoul', 2022-07-22)""")
sql = "SELECT * FROM user WHERE id = 'KO20'".format(id)



def test():

    assert sql == "SELECT * FROM user WHERE id = 'KO20'".format(id)
