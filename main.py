from flask import Flask, render_template, url_for, redirect, request, session, flash
from questions import *
import socket
from dataBaseEngine import *
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = "helloMM"


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:

            try:#try to create object of User when allradiobuttons answered
                user = User(socket.gethostbyname(socket.gethostname()), request.form["pytanie1"], request.form["pytanie2"],
                        request.form["pytanie3"], request.form["pytanie4"])
            except Exception:#try to create object of User when 1 allradiobuttons not answered
                user = User(socket.gethostbyname(socket.gethostname()), request.form["pytanie1"], request.form["pytanie2"],
                            request.form["pytanie3"])
            print(user.returnAnswers())#tutaj będzie wpisywanko do bazy za chwilkę
            try:
                DataBase.insertInto("appDateBaseT.db", user, "mainpage")
            except Exception:
                print("Problem z bazą w 1")
            return redirect(url_for("page1"))
        except Exception:
            print("Bład w mainpage")
            return render_template("mainpage.html")

    else:
        return render_template("mainpage.html")


@app.route('/page1', methods=['POST', 'GET'])
def page1():
    if request.method == 'POST':
        try:
            questions1  = Page1(socket.gethostbyname(socket.gethostname()), request.form["pytanie5"], request.form["pytanie6"], request.form["pytanie7"],
                 request.form["pytanie8.1"], request.form["pytanie8.2"])
            print(questions1.returnAnswers())
            try:
                DataBase.insertInto("appDateBaseT.db", questions1, "page1")
            except Exception:
                print("Błąd wpisywania w bazie page1T")
            return redirect(url_for("page2"))
        except Exception:
            print("Bład w page1")
            return render_template("page1.html")
    else:
        return render_template("page1.html")


@app.route('/page2', methods=['POST', 'GET'])
def page2():
    if request.method == 'POST':
        try:
            try:
                questions2 = Page2(socket.gethostbyname(socket.gethostname()), request.form["pytanie9"],
                                   request.form["pytanie10"], request.form["pytanie11"],
                 request.form["pytanie12"], request.form["pytanie13"])
            except Exception:
                questions2 = Page2(socket.gethostbyname(socket.gethostname()), request.form["pytanie9"],
                                   request.form["pytanie10"], request.form["pytanie11"],
                                   request.form["pytanie12"])
            print(questions2.returnAnswers())#umieść w bazie danych
            try:
                DataBase.insertInto("appDateBaseT.db", questions2, "page2")
            except Exception:
                print("Błąd wpisywania w bazie page2T")
            return redirect(url_for("page3"))
        except Exception:
            print("Bład w page2")
            return redirect(url_for("page2"))
    else:
        return render_template("page2.html")


@app.route('/page3', methods=['POST', 'GET'])
def page3():
    if request.method == 'POST':
        try:
            #obiekt = Page3('jeb', 'czemu', 'to', 'działa', 'teraz?')
            questions3 = Page3(socket.gethostbyname(socket.gethostname()),request.form["pytanie14"],
                               request.form["pytanie15"], request.form["pytanie16"], request.form["pytanie17"])
            print(questions3.returnAnswers())
            try:
                conn = sql.connect("appDataBaseT.db")
                c = conn.cursor()
                c.execute("insert into pageTest values (?, ?, ?, ?, ?)", (questions3.returnAnswers()))
                conn.commit()
                conn.close()
                print("to sie wykonalo")
            except Exception:
                print("Błąd wpisywania w bazie page3T")
                #przekierowanie do nastęnej stronki
            return redirect(url_for("page4"))
        except Exception:
            print("Bład w page3")
            return redirect(url_for("page3"))
    else:
        return render_template("page3.html")


@app.route('/page4', methods=['POST', 'GET'])
def page4():
    if request.method == 'POST':
        try:
            questions4 = Page4(socket.gethostbyname(socket.gethostname()), request.form["pytanie18"], request.form["pytanie19"], request.form["pytanie20"],
                 request.form["pytanie21"], request.form["pytanie22"])
            print(questions4.returnAnswers())#do bazy danych
            try:
                DataBase.insertInto("appDateBaseT.db", questions4, "page4")
            except Exception:
                print("Błąd wpisywania w bazie page4T")
            return redirect(url_for("page5"))
        except Exception:
            print("Bład w page4")
            return redirect(url_for("page4"))
    else:
        return render_template("page4.html")


@app.route('/page5', methods=['POST', 'GET'])
def page5():
    if request.method == 'POST':
        try:
            questions5 = Page5(socket.gethostbyname(socket.gethostname()), request.form["pytanie23"], request.form["pytanie24"], request.form["pytanie25"],
                 request.form["pytanie26"], request.form["pytanie27"])
            print(questions5.returnAnswers())
            try:
                DataBase.insertInto("appDateBaseT.db", questions5, "page5")
            except Exception:
                print("Błąd wpisywania w bazie page5T")
            return redirect(url_for("end"))
        except Exception:
            print("Bład w page5")
            return redirect(url_for("page5"))
    else:
        return render_template("page5.html")

@app.route('/page6')
def end():
    return render_template("page6.html")


class Return:
    def __init__(self):
        self.conn = sql.connect("appDateBaseT.db")
        self.c = self.conn.cursor()
        self.c.execute("select * from page3T")
        self.x = self.c.fetchall()
        self.conn.commit()
        self.conn.close()

    def returnV(self):
        return self.x
if __name__ == "__main__":
    app.run(debug=True)
    ##print("Hello world")

    #obiekt = Page3('192.168.56.1', '5', 'bezzmian', 'niewiem', '5')
    conn = sql.connect("appDataBaseT.db")
    c = conn.cursor()
    #c.execute("""CREATE TABLE pageTest ( id text, pyt14 text, pyt15 text,
    #                                           pyt16 text, pyt17 text ) """)
    #c.execute("insert into pageTest values (?, ? , ? , ? , ?)", (obiekt.returnAnswers()))
    c.execute("select * from pageTest")
    print(c.fetchall())
    #DataBase.insertInto("appDataBaseT.db", obiekt, "page3")
    conn.commit()
    conn.close()
    #print(Return().returnV())
    #print("********")


