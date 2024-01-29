import sqlite3

from flask import g 

def connect_to_database():
    sql=sqlite3.connect("C:/User/Admin/Desktop/Flask Rest API/todoapp.db")
    sql.row_factory=sqlite3.Row
    return 

def get_database():
    if not hasattr(g, "todo_db"):
        g.todo_db = connect_to_database()
    return g.todo_db
