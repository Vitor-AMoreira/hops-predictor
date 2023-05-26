import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


model = pickle.load(open('/var/www/FlaskApp/hopspredictor/beer_model.pkl', 'rb'))
beer_style = pd.read_csv('/var/www/FlaskApp/hopspredictor/beer_style.csv')

def locateBeerRecipe(hop_var, prod_type):
    row = beer_style.loc[(beer_style['Hop variety & % rel. Oil'] == hop_var) & (beer_style['Product Type'] == prod_type)]
    return row




@app.route('/predict/', methods=['POST'])
def predict():
    hop_var = request.get_json().get('hop_var')
    prod_type = request.get_json().get('prod_type')
    amount = request.get_json().get('amount')
    amount = amount.replace(',', '.')
    amount = float(amount)

    if (prod_type == "Whole"):
       prod_type = "T-90/Whole"
    
    if (prod_type == 'T-90'):
       prod_type = "T-90/Whole"

    row = locateBeerRecipe(hop_var, prod_type)

    


    if row.empty:
       return jsonify({
        'No results': 'No results'
        })



    min_total_oil = row.iloc[0]['min total oil']
    min_total_oil = min_total_oil.replace(',', '.')
    min_total_oil = float(min_total_oil)
    min_total_oil = min_total_oil * amount / 100

    mini = [str(row.iloc[0]['min-geraniol']), str(row.iloc[0]['min-linalool']), str(row.iloc[0]['min-myrcene']), str(row.iloc[0]['min-trans-β-Farnesene']), str(row.iloc[0]['min-α-humulene']), str(row.iloc[0]['min-β-Caryophylene']), str(row.iloc[0]['min-β-pinene'])]
    mini = [s.replace(',', '.') for s in mini]
    mini = [float(i) for i in mini]
    mini = [min_total_oil * i * 10 for i in mini]
    print("MINI: ", mini)
    predict_min = model.predict([mini])


    max_total_oil = row.iloc[0]['max total oil']
    max_total_oil = max_total_oil.replace(',', '.')
    max_total_oil = float(max_total_oil)
    max_total_oil = max_total_oil * amount / 100

    maxi = [str(row.iloc[0]['max-geraniol']), str(row.iloc[0]['max-linalool']), str(row.iloc[0]['max-myrcene']), str(row.iloc[0]['max-trans-β-Farnesene']), str(row.iloc[0]['max-α-humulene']), str(row.iloc[0]['max-β-Caryophylene']), str(row.iloc[0]['max-β-pinene'])]
    maxi = [s.replace(',', '.') for s in maxi]
    maxi = [float(i) for i in maxi]
    maxi = [max_total_oil * i * 10 for i in maxi]
    print("MAXI: ", maxi)
    predict_max = model.predict([maxi])


    average_total_oil = row.iloc[0]['average total oil']
    average_total_oil = average_total_oil.replace(',', '.')
    average_total_oil = float(average_total_oil)
    average_total_oil = average_total_oil * amount / 100

    average = [str(row.iloc[0]['average-geraniol']), str(row.iloc[0]['average-linalool']), str(row.iloc[0]['average-myrcene']), str(row.iloc[0]['average-trans-β-Farnesene']), str(row.iloc[0]['average-α-humulene']), str(row.iloc[0]['average-β-Caryophylene']), str(row.iloc[0]['average-β-pinene'])]
    average = [s.replace(',', '.') for s in average]
    average = [float(i) for i in average]
    average = [average_total_oil * i * 10 for i in average]
    print("AVERAGE: ", average)
    predict_average = model.predict([average])


    return jsonify({
        'min_predictions': predict_min.tolist(),
        'max_predictions': predict_max.tolist(),
        'average_predictions': predict_average.tolist()
    })

@app.route('/')
def index():
 return render_template('index.html')

if __name__ == '__main__':
    app.run()
