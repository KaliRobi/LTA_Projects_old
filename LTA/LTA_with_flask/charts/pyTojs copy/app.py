########  imports  ##########
from flask import Flask, jsonify, request, render_template
from time import sleep
import random
app = Flask(__name__)
@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

@app.route('/test', methods=['GET', 'POST']) # ezt a linket keresi a fetch javascript
def testfn():
       # GET request
    if request.method == 'GET':
        message = {'message':'message'} # meghatarozzuk a valtozot
        return jsonify(message)  # itt atalakitjuk jsonna. ez ugy kv parral megy {'message':'message'} . Get eseten ez megy at a masik oldalra.
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

towns = ['Balmazujvaros noi', 'Balmazujvaros feri', 'Hajduboszormeny noi', 'Hajduboszormeny feri', 'hajduszoboszlo noi', 'hajduszoboszlo ferfi', 'Debrecen noi', 'Debrecen ferfi']
nums =  [153.26, 164.27, 153.12, 163.12, 183.74, 163.96, 152.30,  163.80],


@app.route('/getdata/', methods=['GET','POST'])
def data_get():
    
    
    if request.method == 'POST': # POST request
        print(request.get_json())  # parse as json
        return 'OK', 200
    
    else: # GET request
        message = f"towns = {towns}, nums= {nums}"
        
        jsoned= jsonify(message)
        jsonfile = jsoned.get_json()
        print(jsonfile)
        
        return render_template('secpage.html', jsonfile=jsonfile)




app.run(debug=True)

