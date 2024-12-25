#! venv/bin/python3

from flask import Flask, render_template,request
from parse_users_csv import *
from functions import * 
import logging 


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    path = 'users/housemates.csv'
    index_path = 'users/current_id.txt'
    log_path = 'users/log.log'
    data = read_users(path)
    id = get_current_id(index_path)

    if request.method == 'POST':
        if request.form['next'] == "Register Garbage collection":
            name = data['Name'][data['id'] == id].values[0]
            print(name)
            update_log(log_path,name)
            id = iterate(id, 'NEXT', data['id'])
            update_current_id(index_path,id)
            
    name = data['Name'][data['id'] == id].values[0]
    return render_template('index.html', title='Welcome Bois', username=name)

@app.route('/log',methods=['GET', 'POST'])
def logs():
    if request.method == 'POST':
        if request.form["history"] == "view history":
            result = read_logs('users/log.log')
            return render_template('history.html', your_list=result)

if __name__ == "__main__":
    app.run(debug=True, port = 8080)