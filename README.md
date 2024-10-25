# Malware Detection Website

This project is a web application that detects whether a given website URL is safe or potentially malicious. It uses machine learning techniques to classify URLs based on a trained model. The application is built using Flask and scikit-learn.

## **Features**
- **Input any URL** to check if it is safe or potentially harmful.
- **Classifies URLs** using a SVM model trained on a dataset of URLs.
- **Provides a user-friendly interface** with immediate feedback on URL safety.

## **Technologies Used**
- **Flask**: A lightweight WSGI web application framework in Python.
- **Pandas**: A data manipulation and analysis library for Python.
- **Scikit-learn**: A machine learning library for Python, providing simple and efficient tools for data mining and data analysis.
- **Joblib**: A library for saving and loading Python objects, particularly useful for persisting models.
- **HTML/CSS**: For the front-end user interface.

## **Algorithm Used**
- **Random Forest**: Implemented using the `SVC` from scikit-learn.

## **Installation**
1. **Clone the repository**: 
   ```bash
   git clone https://github.com/aniketvamanwalunj/detecting-malware-websites.git

Project Structure
malware-detection/
│
├── app.py                   # Main Flask application
├── train_model.py           # Script to train the machine learning model
├── requirements.txt         # List of project dependencies
├── malware_urls.csv         # Dataset for training the model
├── templates/               # HTML templates for the Flask application
│   ├── index.html           # Home page for URL input
├── model.pkl                # Pre-trained machine learning model
├── vectorizer.pkl           # Vectorizer used to transform URLs into features
├── label_encoder.pkl        # Label encoder for classification
└── README.md                # Project documentation (this file)

##Key Project Details
- **Development Date:** 23-10-2024
- **Accuracy:** 97.13% in detecting malicious URLs.

##Contact
For any questions, suggestions, or feedback, please feel free to reach out:

- **Name:** Aniket Walunj
- **Email:** aniketvamanwalunj@gmail.com
