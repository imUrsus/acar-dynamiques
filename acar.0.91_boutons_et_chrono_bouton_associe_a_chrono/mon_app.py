from flask import Flask, render_template, request, redirect, url_for
from routes import *
from fonctions.chrono import *



app = Flask(__name__)

app.secret_key = "9d263e09465118fcc3b288369ed53396922588fc3e8f466845ef8ab6a00cef25"
app.config['SECRET_KEY'] = "9d263e09465118fcc3b288369ed53396922588fc3e8f466845ef8ab6a00cef25"

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)

