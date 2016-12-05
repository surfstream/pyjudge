
import os
import time
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from requests import get as poll
from sqlalchemy.orm import sessionmaker
from tabledef import *
from werkzeug import secure_filename
from subprocess import run
from multiprocessing import Process
from submission import submit, create_temp_copy, clean_up
import sys
sys.path.insert(0, 'hint/')
from find_similar import find_similar


"""
Main Flask Application, handles the rendering and AJAX calls between server and
client as well as make the necessary calls to interface with the Tango server
to run submitted code from the client.
"""

engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)
user = "hello"
polling_address = "http://localhost:5001/poll/pyjudge/demo/"
tango_input = '../Tango/courselabs/pyjudge-demo/'
tango_output = tango_input + 'output/'


@app.route('/')
def home():
    """
    login portal
    """
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("index.html")


def get_code(code, user):
    """
    Retrieve code from json sent by client send appropriate response
    """
    if code is None:
        return 'Error: unable to retrieve data.'
    return create_temp_copy(user, code['code'])


@app.route("/background_process", methods=['POST'])
def background_process():
    """
    AJAX handling for user submission and interfacing with TANGO,
    """
    try:
        code = request.get_json()
        fname = get_code(code, user)
        if 'Error:' in fname:
            return jsonify(result=fname)
        else:
            p = Process(target=submit, args=(user, fname))
            p.start()
            time.sleep(1)
            pol = poll(polling_address + user + '.out/')
            while 'Output file not found' in pol.text:
                pol = poll(polling_address + user + '.out/')
                time.sleep(1)
            clean_up(user, fname, tango_output)
            return jsonify(result=pol.text)
    except Exception as e:
        return jsonify(str(e))


@app.route("/hint_process", methods=['POST'])
def hint_process():
    """
    AJAX handling for user requesting hint
    """
    try:
        code = request.get_json()
        fname = get_code(code, user)
        if 'Error:' in fname:
            return jsonify(result=fname)
        else:
            all_file = os.listdir(tango_input)
            all_file = [tango_input + i for i in all_file if ".py" in i]
            res = find_similar(fname, all_file)
            output = ''
            for line in open(res, 'r'):
                output += line
            clean_up(user, fname, tango_output)
            return jsonify(result=output)

    except Exception as e:
        return jsonify(str(e))


@app.route('/login', methods=['POST'])
def do_admin_login():
    """
    login and password validation and creating a Session
    """

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(
        User.username.in_(
            [POST_USERNAME]), User.password.in_(
            [POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
        global user
        user = POST_USERNAME
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    """
    logging out from the Session back to the authentication page
    """
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4003)
