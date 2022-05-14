from flask import render_template, redirect, url_for, Blueprint, request


my_view = Blueprint('my_view', __name__)

@my_view.route("/")    
def home():
    return render_template('index.html')

@my_view.route("/admin")   
def admin():
    return render_template('admin.html') 

@my_view.route("/page1")   
def pg1():
    return render_template('page1.html') 

@my_view.route("/page2")   
def pg2():
    return render_template('page2.html') 

@my_view.route("page3")   
def pg3():
    return render_template('page3.html') 

@my_view.route("/page4")   
def pg4():
    return render_template('page5.html') 

@my_view.route("/page5")   
def pg5():
    return render_template('page5.html') 

@my_view.route("/home")
@my_view.route("/js")
@my_view.route("/javascript")
def home_redirect():
    return redirect(url_for("my_view.home"))
