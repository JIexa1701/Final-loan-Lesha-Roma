import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #try:
    int_features = [int(X) for X in request.form.values()]
    #except ValueError:
    #str_features = [str(X) for X in request.form.values()]
    final_features = [np.array(int_features)] 
    #final_features = [np.array(int_features)] + [np.array(str_features)]
    prediction = model.predict(final_features)
    

    output = round(prediction[0], 1)
    
    if output == 1:
        result = 'Bad. Please be careful with this investment!!!'
        
    if output == 0:
        result = 'Good'

    #return render_template('index.html', prediction_text='Loan status is {}'.format(output))
    
    return render_template('index.html', prediction_text='Expected status of the loan is {}'.format(result))

if __name__ == "__main__":
    app.run()
