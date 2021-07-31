########  imports  ##########
from flask import Flask, jsonify, request, render_template
from time import sleep
import random
import json
app = Flask(__name__)
@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('chart_v1.html', embed=example_embed)

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


## THIS IS THE SERVER SIDE. LETS PRETEND THAT THE TWO LISTS BELOW ARE COMMING FROM THE DATABASE. THIS IS ALREADY SET UP IN THE MAIN BRANCH
## THERE IS A FETCH FUCNTION TAKES THE DATA FROM THE SERVER TO THE BROWSER IN EVERY 10 S.
#WATCH THE COLUMNS 


towns2 = ['Balmazujvaros_female', 'Balmazujvaros_male', 'Hajduboszormeny_female', 'Hajduboszormeny_male', 'hajduszoboszlo_female', 'hajduszoboszlo_male', 'Debrecen_female', 'Debrecen_male']
nums2 =  [190.26, 270.27, 150.12, 418.12, 83.74, 243.96, 2.30,  263.80]


combine  =  dict(zip(towns2, nums2))

@app.route('/getdata/', methods=['GET','POST'])
def data_get():
        adat =  combine
        if request.method == 'GET':
            message = adat
            tessage = jsonify(adat)
            return tessage.get_json()



app.run(debug=True)

