from flask import Blueprint
from flask import render_template 
from flask import request, redirect, url_for
from flask import jsonify
import requests

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    name = "menelik and marques"
    return render_template("homepage.html", name = name)

@views.route('/zillow')
def get_zillow_data():
    # url = "https://zillow56.p.rapidapi.com/search"
    # querystring = {"location":"Atlanta, ga","status":"forRent","isApartment":"true","isCondo":"true","doz":"any","onlyWithPhotos":"true"}
    # headers = {
    #     "X-RapidAPI-Key": "2e617df064msh2be268d22e037abp1d77ddjsn18a98458acca",
    #     "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
    # }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # return jsonify(response.json())
    return render_template("zillow.html")

@views.route("/profile")
def profile():
    name = 'Nasir'
    return render_template("profile.html", name = name)

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/signup")
def signup():
    return render_template("signup.html")

@views.route("/login")
def login():
    return render_template("login.html")




@views.route("/protien/<username>")
def prof(username):
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

