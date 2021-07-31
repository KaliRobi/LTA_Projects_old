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


towns2 = ['Balmazujvaros_female', 'Balmazujvaros_male', 'Hajduboszormeny_female', 'Hajduboszormeny_male', 'hajduszoboszlo_female', 'hajduszoboszlo_male', 'Debrecen_female', 'Debrecen_male']
nums2 =  [153.26, 164.27, 153.12, 163.12, 183.74, 163.96, 152.30,  163.80]

nums = [2120, 814, 308,180,24,2]
rels = ['Ref', 'Kat', 'GörK','Izr', 'Ev', 'Feln']


rels2 = ['Ref', 'Kat', 'Izr', 'GörK', 'Ev',]
relnums2 = [155,48,7,6,1,1]

comrel = dict(zip(rels, nums))
comrel2 = dict(zip(rels2, relnums2))

combine  =  dict(zip(towns2, nums2))

@app.route('/getdata/', methods=['GET','POST'])
def data_get():
        adat =  jsonify({"comrel": comrel, "combine": combine, "comrel2": comrel2 })
        if request.method == 'GET':           
            print(type(adat))
            return adat



app.run(debug=True)

