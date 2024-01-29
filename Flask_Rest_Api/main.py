from flask import Flask, render_template, request, redirect, url_for
from database import get_database,connect_to_database

app=Flask(__name__)

@app.route('/')
def index():
    db=get_database()
    task_cursor=db.execute("select * from todolist")
    alltasks = task_cursor.fetchall()

    return render_template("index.html")
@app.route('/inserttask', methods=["POST","GET"])
def inserttask():
    if request.method=="POST":
        enteredtask=request.form['tordaystask']
        db = get_database()
        db.execute("inser into todolist (tesk) values(?)",[enteredtask])
        db.commit()
        return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/deletetask/<int:id>", methods=["POST","GET"])
def deletetask(id):
    if request.method=="GET":
        db = get_database()
        db.execute("delete from todolist where id =?",[id])
        db.commit()
        return redirect(url_for("index"))
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)