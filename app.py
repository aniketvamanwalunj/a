"""
Created on Monday, 14 Oct 2024

@author: Aniket
"""

from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the saved model, vectorizer, and label encoder
model = joblib.load('svm_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        
        try:
            # Vectorize the input URL
            url_vectorized = vectorizer.transform([url])
            prediction = model.predict(url_vectorized)
            label = label_encoder.inverse_transform(prediction)[0]
            
            if label == 'benign':
                result = 'The website is Safe!'
                result_class = 'safe'
            else:
                result = 'The website is not safe!'
                result_class = 'not-safe'
                
            return render_template('index.html', result=result, result_class=result_class)
        
        except Exception as e:
            return f"An error occurred: {str(e)}"

@app.route('/project_details')
def project_details():
    return render_template('project_details.html')

if __name__ == "__main__":
    # Allow Flask to be accessible from other devices on the same network
    app.run(host='0.0.0.0', port=5000)  # You can change the port if needed
