from flask import Blueprint
from flask import render_template 
from flask import request, redirect, url_for
from flask import jsonify
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    name = "menelik and marques"
    return render_template("index.html", name = name)

@views.route("/profile/<username>")
def profile(username):
    args = request.args
    name = args.get('name')
    return render_template("index.html", name = username)

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route('/json')
def get_json():
    return jsonify({'name': 'tim', 'coolness' : 10})


@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for("views.home"))

