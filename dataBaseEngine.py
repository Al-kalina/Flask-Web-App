import sqlite3 as sql

class DataBase:
    def __init__(self, baza):
        pass

    @staticmethod
    def createTables():

        conn = sql.connect("appDataBaseT.db")
        c = conn.cursor()
        try:
            try:
                c.execute("""CREATE TABLE userT (id text , age text, sex text, university text, 
                faculty text)""")
            except Exception:
                print("Coś nie tak z user")
            try:
                c.execute("""CREATE TABLE page1T (id text, pyt5 text, pyt6 text, pyt7 text,
                                            pyt8_1 text, pyt8_2 text )""")
            except Exception:
                print("coś nie tak z page1T")
            try:
                c.execute("""CREATE TABLE page2T ( id text, pyt9 text, pyt10 text, pyt11 text,
                                            pyt12 text, pyt13 text)""")
            except Exception:
                print("coś nie tak z page2T")
            try:
                c.execute("""CREATE TABLE page3T ( id text, pyt14 text, pyt15 text,
                                            pyt16 text, pyt17 text ) """)
            except Exception:
                print("coś nie tak z page3T")
            try:
                c.execute("""CREATE TABLE page4T ( id text, pyt18 text, pyt19 text, pyt20 text, 
                                        pyt21 text, pyt22 text )""")
            except Exception:
                print("coś nie tak z page4T")
            try:
                c.execute("""CREATE TABLE page5T ( id text,  pyt23 text, pyt24 text,
                                            pyt25 text, pyt26 text, pyt27 text ) """)
            except Exception:
                print("coś nie tak z page5T")
        except Exception:
            print("Sth went wrong")

        finally:
            conn.commit()
            conn.close()


    @staticmethod
    def checkIP(baza, ip):
        conn = sql.connect(baza)
        c = conn.cursor()
        c.execute("SELECT COUNT() FROM user WHERE ip = ?", (ip,))
        x = c.fetchone()[0]
        conn.commit()
        conn.close()
        if x == 0:
            return True
        else:
            return False



    @staticmethod
    def returnNextId(baza):
        conn = sql.connect(baza)
        c = conn.cursor()
        c.execute("SELECT COUNT() FROM user")
        currentId = c.fetchone()[0]
        conn.commit()
        conn.close()
        return int(currentId)+1

    @staticmethod
    def insertIP(baza, ip):
        conn = sql.connect(baza)
        c = conn.cursor()
        c.execute("INSERT INTO IP values (?)", (ip,))
        conn.commit()
        conn.close()

    @staticmethod
    def insertInto(baza, obj, option):
        conn = sql.connect(baza)
        c = conn.cursor()
        try:
            if option == 'mainpage':
                c.execute("INSERT INTO userT values (?, ?, ?, ?, ?)", (obj.returnAnswers()))
            elif option == 'page1':
                c.execute("INSERT INTO page1T values (?, ?, ?, ?, ?, ?)", (obj.returnAnswers()))
            elif option == 'page2':
                c.execute("INSERT INTO page2T values (?, ?, ?, ?, ?, ?)", (obj.returnAnswers()))
            elif option == 'page3':
                c.execute("insert into pageTest values (?, ? , ? , ? , ?)", (obj.returnAnswers()))
            elif option == 'page4':
                c.execute("INSERT INTO page4T values (?, ?, ?, ?, ?, ?)", (obj.returnAnswers()))
            elif option == 'page5':
                c.execute("INSERT INTO page5T values (?, ?, ?, ?, ?, ?)", (obj.returnAnswers()))
        except Exception:
            print("Wystąpił wyjątek z funkcji insertInto")
        finally:
            conn.commit()
            conn.close()

