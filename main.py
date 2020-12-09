from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def get():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

    querystring = {"q": "NBCC", "region": "IN"}

    headers = {
        'x-rapidapi-key': "9ab78cf628msh9d4d4908d10f6bcp1fd9e4jsn7285c74c32e4",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

    #print(response.text)


app.run(debug=True)



