from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
from werkzeug import secure_filename
import subprocess
engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)
user="hello"
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("quiz.html")
'''@app.route()
def home2(POST_USERNAME):
    if not session.get('logged in'):
        return render_template('login.html')
    else:
        return render_template("quiz.html")'''         

@app.route('/uploader',methods=['GET','POST'])
def upload_file():
    #global user
    if request.method=='POST':
        f=request.files['file']

        global user     
        submit=user+"_"+"dum.py"
        f.save(submit)

        #return 'file uploaded successfully'

        str="python "+submit+"<"+"input.txt"+">"+ user+"_"+"result.txt"
        status,output=subprocess.getstatusoutput(str)
        if status!=0:
           # return '<a href="http://localhost:4000/logout" class="button">Logout</a>file uploaded successfully but problem in execution '
             return output            
        else:
            return '<a href="http://localhost:4000/logout" class="button">Logout</a> file uploaded successfully and executed successfully '   
    

def home2():
    if session['logged_in']==False:
        return render_template("login.html")
    else:
        return render_template("quiz.html") 

                   
 
@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        global user
        user=POST_USERNAME
    else:
        flash('wrong password!')
    return home2()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()    
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)