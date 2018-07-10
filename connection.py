import pymysql


def connection():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Database_Password",
                           db="example",
                           use_unicode=True,
                           charset="utf8")
    c = conn.cursor()
    return c, conn


def dict_connection():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Sriteja@27",
                           db="example",
                           use_unicode=True,
                           charset="utf8",
                           cursorclass=pymysql.cursors.DictCursor
                           )
    c = conn.cursor()
    return c, conn
