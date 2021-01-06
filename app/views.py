import datetime
import json

import requests
from flask import render_template, redirect, request
from random import randint
from app import app

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []


def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)

"""
the index page for the users.
127.0.0.1:5000
"""
@app.route('/push')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='ID-STORE ',
                                 # 'content sharing',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        matricule = request.form["matricule"]
        password = request.form["password"]
        global users
        if matricule in matricule and password in password:
            return render_template("choice.html", name=matricule)
        else:
            render_template("user-login.html")
    return render_template("user-login.html")

"""
qr page
127.0.0.1:5000/b
"""
@app.route('/qr')
def qr():
    fetch_posts()
    name = "Franklin"
    return render_template('qr.html',
                           title='Data encrypted on QR code',
                                 # 'content sharing',
                           posts=posts,
                           name=name,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)

"""
dashboard page
127.0.0.1:5000/b
"""
@app.route('/')
def dashboard():
  
    name = "Franklin"
    fetch_posts()
    return render_template('dashboard.html',
                           title='Data encrypted on QR code',
                                 # 'content sharing',
                           posts=posts,
                           name=name, 
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    # file = request.form["file"]
    # file.save('static/storages/{}/{}/{}'.format(author,randint(1000,8000), file.filename))
    author = request.form["author"]

    post_object = {
        'author': author,
        'content': post_content,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')
