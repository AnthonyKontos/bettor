from flask import Flask, render_template, redirect, url_for, request, jsonify
from cassandra.cluster import Cluster
import time
from operator import itemgetter
import pandas as pd
import numpy as np
import time
import json
import datetime
import calendar
import random
import pytz
from pytz import timezone
utc=pytz.utc
eastern=pytz.timezone('US/Eastern')


app = Flask(__name__)

cluster = Cluster(['54.67.105.220'])
session = cluster.connect('betData')


@app.route('/')
@app.route('/welcome')
def welcome():
    url_for('static', filename='jquery.datetimepicker.css')
    url_for('static', filename='jquery.datetimepicker.js')
    return render_template("main.html")

@app.route('/calculator')
def calculator(stockName):
    rowTime = sessionTwitterSeries.execute("select * from trendingminute where ticker= '" + stockName + "' ")
    data1 = []
    data2  = []
    for r in rowTime:    
        a = [calendar.timegm(datetime.datetime(r.year, r.month, r.day,r.hour,r.minute).timetuple())*1000, r.frequency]

        ss = 0
        if r.sentiment > 0:
            ss = 1
        else:
            if r.sentiment <0:
                ss = -1

        b = [calendar.timegm(datetime.datetime(r.year, r.month, r.day,r.hour,r.minute).timetuple())*1000, ss]
        data1.append(a)
        data2.append(b)

    data1.reverse()
    data2.reverse()
    text = 'Number of tweets/sentiment for '+stockName

    return jsonify(data1=data1, data2=data2, text=text)   

@app.route('/currentlines/<stockName>')
def current_lines(stockName):
    favs = session.execute("select * from currentLines where result= 'W' and event= '" + event + "' and market= '" + market + "' ")
    fdata = []

    udogs = session.execute("select * from currentLines where result= 'L' and event= '" + event + "' and market= '" + market + "' ")
    udata = []

    text = 'Stock Price/ Mentions for '+stockName

    return jsonify(data1=fdata, data2=udata, text=text)   

def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            pass # do something
        elif request.form['submit_button'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)