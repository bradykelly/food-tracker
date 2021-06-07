import sqlite3
from flask import g

def connect_db():
    sql = sqlite3.connect(
        "D:/Personal/Python Courses/Udemy/Ultimate Flask Course/food-tracker/food_log.db")
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, "sqlite3"):
        g.sqlite3 = connect_db()
    return g.sqlite3