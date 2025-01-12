from sqlite3 import connect, Error

def InsertUserlar(first_name):# first_name, telegram_id, url='None', username='None'
    try:
        c = connect('test.db')
        cursor = c.cursor()
        cursor.execute("""insert into userlar(first_name) values(?)""", (first_name,))
        c.commit()
        cursor.close()
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if c:
            c.close()
# InsertUserlar("Javohir")



def ReadObunachilar():
    try:
        c = connect('test.db')
        cursor = c.cursor()
        cursor.execute("select count(*) from userlar;")
        a = cursor.fetchall()
        cursor.close()
        return a
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if c:
            c.close()
# print(ReadObunachilar())


def ReadObunachilars():
    try:
        c = connect('test.db')
        cursor = c.cursor()
        cursor.execute("select * from userlar;")
        a = cursor.fetchall()
        cursor.close()
        return a
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if c:
            c.close()



# try:
#     con = connect('test.db')
#     cursor = con.cursor()
#     cursor.execute("""
#             create table userlar(
#                 ID INTEGER PRIMARY KEY NOT NULL,           
#                 first_name text not null
#                 ); """)
#     con.commit()
#     cursor.close()
# except (Error, Exception) as eror:
#     print("Eror", eror)
# finally:
#     if con:
#         con.close()
#         print("Tugadi")