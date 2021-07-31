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

towns2 = ['almazujvaros noi', 'Balmazujvaros ferfi', 'Hajduboszormeny noi', 'Hajduboszormeny feri', 'hajduszoboszlo noi', 'hajduszoboszlo ferfi', 'Debrecen noi', 'Debrecen ferfi']
nums2 =  [153.26, 164.27, 153.12, 163.12, 183.74, 163.96, 152.30,  163.80]


combine  =  dict(zip(towns2, nums2))



@app.route('/getdata/', methods=['GET','POST'])
def data_get():
        adat =  combine
        if request.method == 'GET':
            message = adat
            tessage = jsonify(adat)
            print(type(tessage))
            print(tessage.get_json())
            return tessage.get_json()
            
        # jsoned= jsonify(nums)

        # print(type(jsoned))
        # jsonfile = jsoned.get_json()
        # # print(type(jsonfile))
        # # print(jsonfile)
        
        # return render_template('chart_v1.html', jsonfile=nums)




app.run(debug=True)

