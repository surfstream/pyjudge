"""
Main Flask Application, handles the rendering and AJAX calls between server and
client as well as make the necessary calls to interface with the Tango server
to run submitted code from the client.

If the user code is correct or faulty Tango will output respectively
and the results will be displayed to the user.

Similarly to the hinting, as it stands written, the user will be provided with
the shortest or most similar solution
"""

import os   #used for retrieving list of files in  directory
import time #used to sleep main thread, in order to not flood Tango w/ requests
import sys  #used to import files in "./hint", a directory down
from flask import Flask, flash, redirect, render_template
from flask import request, session, abort, jsonify
from requests import get as poll #used solely to poll Tango server's termination
from sqlalchemy.orm import sessionmaker
from tabledef import *
from werkzeug import secure_filename
from multiprocessing import Process #used to separate a proc from main thread
from submission import submit, create_temp_copy, clean_up #summision work

#import files for the hinting process
sys.path.insert(0, 'hint/')
from find_similar import find_similar #used for hinting process



#app-wide variables
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
        #retireve the code sent by the client via an AJAX POST call. If code is
        #sent the name of the temporary file created will be returned
        code = request.get_json()
        fname = get_code(code, user)
        if 'Error:' in fname:
            #notify the user of an error if code not received
            return jsonify(result=fname)
        else:
            #create a process outside to run the submission code
            p = Process(target=submit, args=(user, fname))
            p.start()
            #call on a sleep to allow the Tango server the time to process
            time.sleep(1)
            #begin the loop to poll the server on when the job is finished
            #pol.text contains the resulting output of the server
            pol = poll(polling_address + user + '.out/')
            while 'Output file not found' in pol.text:
                pol = poll(polling_address + user + '.out/')
                time.sleep(1)
            #clean up once output is generated
            clean_up(user, fname, tango_output)
            #return the results to the user
            return jsonify(result=pol.text)
    except Exception as error:
        return jsonify(str(error))


@app.route("/hint_process", methods=['POST'])
def hint_process():
    """
    AJAX handling for user requesting hint
    """
    try:
        #same as above, couldn't modularize due to errors being raised
        code = request.get_json()
        fname = get_code(code, user)
        if 'Error:' in fname:
            return jsonify(result=fname)
        else:
            #retrieve a list of files in the Tango Server
            all_file = os.listdir(tango_input)
            #filter out any non python code and and append them to the path
            all_file = [tango_input + i for i in all_file if ".py" in i]
            #retrieve the file most similar to the current client code
            res = find_similar(fname, all_file)
            #generate output for the user based on the file most similar
            output = ''
            for line in open(res, 'r'):
                output += line
            #clean up and return the result to the user
            clean_up(user, fname, tango_output)
            return jsonify(result=output)
    except Exception as error:
        return jsonify(str(error))


@app.route('/login', methods=['POST'])
def do_admin_login():
    """
    login and password validation and creating a Session
    """

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    sess = Session()
    query = sess.query(User).filter(
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
    """
    Main function calling on the creation and instantiation of the flask server
    """
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4003)
