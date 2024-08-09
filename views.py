from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return "home page"

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/register")
def register():
    return render_template("register.html")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.html", name=name)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))