
import numpy as np
import pickle
from flask import Flask, request, render_template
import numpy.random._pickle

app = Flask(__name__,template_folder='templates/')
model = pickle.load(open('Model/model.pkl','rb'))

@app.route('/')
def careDemia():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():

    if request.method == "GET":
        return render_template('form.html')
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    print(array_features)
    print(request.form.values)
    prediction = model.predict(array_features)
    output = prediction

    if output == 1:
        return render_template('form.html', result = 'The patient is not likely to have breast cancer!')
    else:
        return render_template('form.html', result= 'The patient is likely to have breast cancer!')


if __name__ == '__main__':
   app.run(debug=True)