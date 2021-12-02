from flask import *
import sqlite3
window=Flask(__name__)
@window.route("/")
def index():
    return render_template("index.html")
@window.route("/add")
def add():   
    return render_template("add.html")
@window.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            pubisher = request.form["pubisher"]
            bookname = request.form["bookname"]
            author = request.form["author"]
            total = request.form["total"]
            with sqlite3.connect("librarybook1.db") as con:
                cur = con.cursor()   
                cur.execute("INSERT into book1 (pubisher,bookname,author,total ) values (?,?,?,?)",(pubisher,bookname,author,total))
                con.commit()
                msg = "Books Returned Successfully"   
        except:
            con.rollback()
            msg = "Can't able to return,Please Recontinue'"
        finally:
            return render_template("success.html",msg = msg)
            con.close()

@window.route("/books")
def books():
    con = sqlite3.connect("librarybook1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select id,pubisher,bookname,author,total from book1")   
    rows = cur.fetchall()
    return render_template("display.html",rows = rows)
@window.route("/search")
def search():
    return render_template("search.html")
@window.route("/getdetails",methods=["POST"])
def getdetails():
    bookname= request.form["bookname"]
    with sqlite3.connect("librarybook1.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from book1 where bookname = ?",(bookname,))
        rows=cur.fetchall()
        return render_template("searchresult.html",rows=rows)
@window.route("/borrow")
def borrow():
    return render_template("borrow.html")
@window.route("/deleterecord",methods= ["POST"])   
def deleterecord():
    bookname = request.form["bookname"]
    with sqlite3.connect("librarybook1.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from book1 where bookname = ?",(bookname,))
            msg = "BOOK IS AVAILBALE GO AND GET THE BOOK"   
        except:
            msg = "BOOK IS NOT AVAILABLE CAN'T ABLE TO GET IT"
        finally:
            return render_template("delete_record.html",msg = msg)
@window.route("/author")
def author():
    return render_template("author.html")

@window.route("/authordetails",methods=["POST"])
def authordetails():
    author= request.form["author"]
    with sqlite3.connect("librarybook1.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from book1 where author = ?",(author,))
        rows=cur.fetchall()
        return render_template("authorresult.html",rows=rows)
if __name__=="__main__":
    window.run(debug=True)
