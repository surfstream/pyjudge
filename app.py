import os
import time
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from requests import get as poll
from sqlalchemy.orm import sessionmaker
from tabledef import *
from werkzeug import secure_filename
from subprocess import run
from multiprocessing import Process
from submission import submit

engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)
user="hello"
polling_address = "http://localhost:5001/poll/pyjudge/demo/"
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("index.html")


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
                return jsonify(result='Error detrieving data.')
            else:
                fname = user + '_primes.py'
                f = open(fname, 'w')
                f.write(code['code'])
                f.close()
                print("submission")
                p = Process(target=submit, args=(user, fname))
                p.start()
                p.join()
                pol = poll(polling_address+user+'.out/')
                while 'Output file not found' in pol.text:
                    pol = poll(polling_address+user+'.out/')
                    time.sleep(1)
                outf = open(user+'.out', 'w')
                string = str(pol.text)
                outf.write(string)
                outf.close()
                #outf = open("admin.out", 'w')
                #for line in open('../Tango/courselabs/pyjudge-demo/output/'+user+'.out', 'r'):
                #    outf.write(line)
                #outf.close()
                run(['rm', '../Tango/courselabs/pyjudge-demo/output/'+user+'.out'])
                #return "hello World"
                return jsonify(result=string)
    except Exception as e:
        return str(e)        


@app.route("/hint_process", methods=['GET', 'POST'])
def hint_process():
    try:
        pass
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
