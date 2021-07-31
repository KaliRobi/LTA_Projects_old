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

data = list(range(400,900,6))
print(data)


@app.route('/getdata/<index_no>', methods=['GET','POST'])
def data_get(index_no):
    dat = data[int(index_no)]
    
    if request.method == 'POST': # POST request
        print(request.get_text())  # parse as text
        return 'OK', 200
    
    else: # GET request
       t = f"{index_no}, {dat}"
       return render_template('secpage.html', embed=t)




app.run(debug=True)

