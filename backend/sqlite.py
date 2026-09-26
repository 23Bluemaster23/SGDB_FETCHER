import sqlite3

from configuration.constants import DB_LOCATION

def import_from_lutris():
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()
