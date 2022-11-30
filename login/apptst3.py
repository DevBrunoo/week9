# Implements a registration form, storing registrants in a SQLite database, with support for deregistration

from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///froshims.db") #Sintaxe simples que se refere ao protocolo SQLite "Usa SQLite para conversar com um arquivo localmente". A duas primeiras barras e como vemos normalmente a terceira se baseia na pasta atual

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)