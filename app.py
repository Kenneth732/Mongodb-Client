from flask import Flask, render_template, redirect, request, url_for

from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos