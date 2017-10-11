from flask import Flask, render_template, redirect, url_for, request
import sqlite3 as sql
import hashlib
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/fworkshop")
def free():
    return render_template("fworkshop.html")

@app.route("/uworkshop")
def upcoming():
    return render_template("uworkshop.html")


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':
     try:
        
         name = request.form['collegename']
         cont = request.form['contact']
         appdate=request.form['date']
         dept=request.form['department']
         duration=request.form['duration']
         wtopic=request.form['workshoptopic']
         followup1=request.form['followup1']
         remark1=request.form['remark1']
         followup2=request.form['followup2']
         remark2=request.form['remark2']



         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO upcoming_workshop (name,cont,appdate,dept,duration,wtopic,followup1,remark1,followup2,remark2) VALUES (?,?,?,?,?,?,?,?,?,?)",(name,cont,appdate,dept,duration,wtopic,followup1,remark1,followup2,remark2) )
            
            con.commit()
            msg = "Record successfully added"
     except:
         con.rollback()
         msg = "error in insert operation"
      
     finally:
        return render_template("result.html",msg = msg)
        con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from upcoming_workshop")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)






@app.route('/addrecord',methods = ['POST', 'GET'])
def addrecord():
  if request.method == 'POST':
     try:
         srno=request.form['srno']
         collegename=request.form['collegename']
         seminardate=request.form['seminardate']
         hod=request.form['hod']
         department=request.form['department']
         expectation=request.form['expectation']
         mail=request.form['mail']
         reply=request.form['reply']
         followup1=request.form['followup1']
         remark1=request.form['remark1']
         followup2=request.form['followup2']
         remark2=request.form['remark2']



         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO free_workshop (srno,collegename,seminardate,hod,department,expectation,mail,reply,followup1,remark1,followup2,remark2)  VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(srno,collegename,seminardate,hod,department,expectation,mail,reply,followup1,remark1,followup2,remark2) )
            
            con.commit()
            msg = "Record successfully added"
     except:
         con.rollback()
         msg = "error in insert operation"
      
     finally:
        return render_template("fresult.html",msg = msg)
        con.close()

@app.route('/flist')
def flist():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from free_workshop")
   
   rows = cur.fetchall();
   return render_template("flist.html",rows = rows)


@app.route('/secret')
def secret():
    return "This is a secret page!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/mworkshop")
def monthly():
    return render_template("mworkshop.html")

@app.route("/briefoverview")
def overview():
    return render_template("briefoverview.html")



if __name__ == "__main__":
    app.run(debug = True)
