import mysql
from mysql.connector import Error
from DB import config


def __connect():
    """ Connect to MySQL database """
    try:

        print('Connected to MySQL database...')
        conn = mysql.connector.connect(**config.settings)
        if conn.is_connected():
            print('Successful')
            return conn

    except Error as e:
        print(e)


def select_all():
    try:
        con = __connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM dishes")
        print('Select all...')
        rows = cursor.fetchall()
        result = []

        for row in rows:
            product = {'id': row[0],
                       'struct_id': row[1],
                       'name': row[2],
                       'img': row[3],
                       'price': row[4]}

            result.append(product)

        return result

    except Error as e:
        print(e)


def select_structure():
    con = __connect()
    cursor = con.cursor()
    result = []
    cursor.execute("SELECT d.id,m.name, d2.name, v.name, s.name "
                   "FROM structure "
                   "JOIN dishes d on structure.id = d.struct_id "
                   "JOIN meat m on m.id = structure.meat_id "
                   "join dough d2 on d2.id = structure.dough_id "
                   "join vegetables v on v.id = structure.vegetables_id "
                   "join spice s on s.id = structure.spice_id")
    rows = cursor.fetchall()
    for i in rows:
        structure = {'id': i[0],
                     'meat': i[1],
                     'dough': i[2],
                     'veg': i[3],
                     'spice': i[4]}
        result.append(structure)
        print(result)

    return result
