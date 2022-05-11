from flask import Flask, render_template, redirect,Blueprint  #flask imports
from views import my_view

app = Flask(__name__) 

app.register_blueprint(my_view) #sets the blueprint

@app.errorhandler(Exception)
def page_not_found(e):
    return render_template("404.html", e=e)

if __name__=="__main__":
    app.run(debug=True, port=8000) # debugging is activated and the project is set to hosted on port 8000 (debugging should only be used in testing).

# folder structure should be:
#     main_folder
#         virtual env folder - we activate it, and that's it!
#         static folder
#             you can define more folders here if you like!
#             static files like style.css
#         templates folder
#             html files like base.html, index - anything we return with render_template
#         app.py
#         views.py