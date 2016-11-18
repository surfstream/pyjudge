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
        return render_template("index.html")
   
    

"""def home2():
    if not session.get['logged_in']==False:
        return render_template("login.html")
    else:
        return render_template("index.html")"""

@app.route("/background_process", methods=['GET', 'POST'])
def background_process():
    try:
        if request.method == 'GET':
            lang = request.args.get('proglang', 0, type=str)
            if lang.lower() == 'python':
                return jsonify(result='You are wise')
            else:
                return jsonify(result='Try again.')
        elif request.method == 'POST':
            code = request.get_json()
            if code == None:
                return jsonify(result='error retrieving data')
            else:
                f = open(user+".py", 'w')
                f.write(code['code'])
                f.close()   
                return jsonify(result=code['code'])
    except Exception as e:
        return str(e)        

                   
 
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
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()    
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4003)