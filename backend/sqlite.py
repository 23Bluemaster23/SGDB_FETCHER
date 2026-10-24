import sqlite3

from backend import configparser
from configuration.constants import DB_LOCATION
import os

def import_from_lutris():
    delete_database()
    con = sqlite3.connect(configparser.get_config('DB','lutris'))
    cur = con.cursor()
    cur.execute('SELECT name,slug FROM games;')
    lutris_data = cur.fetchall()
    cur.close()
    con.close()

    new_data = [game + ('lutris',) for game in lutris_data]

    con = create_database()
    cur = con.cursor()
    cur.executemany("""
        INSERT INTO games (name,slug,launcher)
        VALUES (?,?,?)""",new_data)
    con.commit()
    con.close()

def delete_database():
    if os.path.exists(DB_LOCATION):
        try:
            os.remove(DB_LOCATION)
        except PermissionError:
            print("No tiene los permisos necesarios para eliminar")
def create_database():
        con = sqlite3.connect(DB_LOCATION)
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                slug TEXT NOT NULL,
                launcher TEXT NOT NULL,
                sgdb_id INTEGER
            );""")
        con.commit()
        return con

def get_games():
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()

    cur.execute('SELECT id,name,slug,launcher FROM games;')
    return cur.fetchall()

def get_game(id:int):
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()

    cur.execute('SELECT id,name,slug,launcher,sgdb_id FROM games WHERE id=?;',[id])
    return cur.fetchone()

def set_game_data(id:int,key:str,value:str):
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()
    cur.execute(f'UPDATE games SET {key} = ? WHERE id = ?',(value,id))
    con.commit()
    con.close()

# if __name__ == '__main__':
#     import_from_lutris()
#     print(get_games())
#     set_game_data(1,'sgdb_id','NULL')
