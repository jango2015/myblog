#!/usr/bin/env python
# encoding: utf-8

from myblog import app
from flask import render_template,flash, redirect


@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
