#encoding: utf-8
import pymysql

from flask import Flask, g, render_template

app = Flask(__name__)

def index():
    # Si el usuario se logeo
    return render_template("user/home.html")
    # Sino deberia ir al login
