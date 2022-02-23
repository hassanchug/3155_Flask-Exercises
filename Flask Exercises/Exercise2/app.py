# Name: Hassan Chughtai 
# Group Members: Paul Thottappilly, Ivory Steed, Tony Le, Shekar Balasubramaniam  
# Used the zoom recording as my resource

from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/') # sets route to the home.html
def home():
    return render_template('home.html') 

@app.route('/calculate') # sets route to the calculate.html
def calc(nums=None): 
    if len(request.args)==0:
        return render_template('calculate.html') 
    nums = request.args['nums'] 
    try: # Checks if num is even or odd
        if int(nums)%2==0: 
            msg=' num is even'
        elif int(nums)%2!=0: 
            msg=' num is odd'
    except: # if not says that it is not an integer
        msg='num is not an integer!'
    return render_template('calculate.html', num=nums, name=msg) 

if __name__ == "__main__":
    app.run()