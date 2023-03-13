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

cluster = Cluster(['127.0.0.1'], port=9042, control_connection_timeout=60)
session = cluster.connect()

@app.route('/')

@app.route('/calculator')
def calculator(stockName):
    fav = session.execute("select participant, sportsbook, american_odds, inverse_odds, profit from betData.currentLines where date= '" + dt + "' and market_id= '" + mid + "' and result= 'W'")
    udog = session.execute("select participant, sportsbook, american_odds, inverse_odds, profit from betData.currentLines where date= '" + dt + "' and market_id= '" + mid + "' and result= 'L'")


if __name__ == '__main__':
    app.run(debug=True)