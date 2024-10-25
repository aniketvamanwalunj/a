"""
Created on Tuesday, 15 Oct 2024

@author: Aniket
"""

from flask import Flask, request, render_template
import joblib

# Step 1: Initialize the Flask app
app = Flask(__name__)

# Step 2: Load the trained model and vectorizer
try:
    model = joblib.load('svm_model.pkl')  # Ensure you use correct model file names
    vectorizer = joblib.load('vectorizer.pkl')
except Exception as e:
    print(f"Error loading model or vectorizer: {e}")

# Step 3: Define the route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Step 4: Define the route for processing URL checks
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form.get('url')  # Get the URL from the form
        if url:  # Check if the input is not empty
            try:
                data = [url]  # Prepare data for vectorization
                vect = vectorizer.transform(data)  # Vectorize the input URL
                prediction = model.predict(vect)  # Predict using the model

                # Step 5: Return the result
                if prediction[0] == 0:
                    result = "The website is safe!"
                else:
                    result = "The website is not safe!"
            except Exception as e:
                result = f"An error occurred during prediction: {e}"
        else:
            result = "Please enter a valid URL!"

        return render_template('index.html', result=result)

# Step 6: Run the app
if __name__ == "__main__":
    app.run(debug=True)
