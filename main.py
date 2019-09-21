import os
import sys

from flask import Flask, redirect, render_template, request

from google.cloud import firestore
from google.cloud import storage
from google.cloud import vision


app = Flask(__name__)


@app.route('/')
def homepage():
    print ("Hello World")