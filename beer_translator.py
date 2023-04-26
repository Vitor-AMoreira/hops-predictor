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


model = pickle.load(open('beer_model.pkl', 'rb'))
beer_style = pd.read_csv('beer_style.csv')

def locateBeerRecipe(hop_var, prod_type):
    row = beer_style.loc[(beer_style['Hop variety & % rel. Oil'] == hop_var) & (beer_style['Product Type'] == prod_type)]
    return row

row = locateBeerRecipe('Centennial', 'Cryo')


@app.route('/predict/<string:hop_var>/<string:prod_type>', methods=['POST'])
def beer_predict(hop_var, prod_type):
    row = locateBeerRecipe(hop_var, prod_type)
    print(row)
    mini = [str(row.iloc[0]['min-geraniol']), str(row.iloc[0]['min-linalool']), str(row.iloc[0]['min-myrcene']), str(row.iloc[0]['min-trans-β-Farnesene']), str(row.iloc[0]['min-α-humulene']), str(row.iloc[0]['min-β-Caryophylene']), str(row.iloc[0]['min-β-pinene'])]
    mini = [s.replace(',', '.') for s in mini]
    mini = [float(i) for i in mini]
    predict_min = model.predict([mini])
    maxi = [str(row.iloc[0]['max-geraniol']), str(row.iloc[0]['max-linalool']), str(row.iloc[0]['max-myrcene']), str(row.iloc[0]['max-trans-β-Farnesene']), str(row.iloc[0]['max-α-humulene']), str(row.iloc[0]['max-β-Caryophylene']), str(row.iloc[0]['max-β-pinene'])]
    maxi = [s.replace(',', '.') for s in maxi]
    maxi = [float(i) for i in maxi]
    predict_max = model.predict([maxi])
    average = [str(row.iloc[0]['average-geraniol']), str(row.iloc[0]['average-linalool']), str(row.iloc[0]['average-myrcene']), str(row.iloc[0]['average-trans-β-Farnesene']), str(row.iloc[0]['average-α-humulene']), str(row.iloc[0]['average-β-Caryophylene']), str(row.iloc[0]['average-β-pinene'])]
    average = [s.replace(',', '.') for s in average]
    average = [float(i) for i in average]
    predict_average = model.predict([average])
    return jsonify({
        'min_predictions': predict_min.tolist(),
        'max_predictions': predict_max.tolist(),
        'average_predictions': predict_average.tolist()
    })

@app.route('/')
def index():
 return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

