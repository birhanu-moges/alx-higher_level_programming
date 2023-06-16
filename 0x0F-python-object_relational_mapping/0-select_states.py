#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT * FROM `states`")
    for state in con.fetchall():
        print(state)
    con.close()
    db.close()
