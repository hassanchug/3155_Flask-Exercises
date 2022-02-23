# Name: Hassan Chughtai 
# Group Members: Paul Thottappilly, Ivory Steed, Tony Le, Shekar Balasubramaniam  
# Used the zoom recording as my resource
from flask import Flask, render_template

import calendar
import datetime

app = Flask(__name__)

@app.route('/') # route to the index.html file 
def index():
    curr_time = datetime.datetime.now() # sets current time to the time as of now 
    timecurrent = curr_time.strftime("%B %d %Y %H:%M:%S") # formats the time 
    return render_template('index.html', timecurrent = calendar.day_name[curr_time.weekday()] + ', ' +timecurrent) # returns the formatted time

if __name__ == '__main __':
    app.run()