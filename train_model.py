"""
Created on Tuesday, 15 Oct 2024

@author: Aniket
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load dataset with low_memory=False to avoid DtypeWarning
df = pd.read_csv('D:/MalwareDetection/SVM/malware_urls.csv', low_memory=False)

# Step 2: Handle NaN values
df = df.dropna(subset=['url', 'label'])

# Step 3: Preprocessing - Encode labels
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])

# Step 4: Vectorize URLs using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['url'])  # Ensure no NaN values

y = df['label']

# Step 5: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the model using SVM
model = SVC(kernel='linear')  # You can try 'rbf', 'poly' or other kernels
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy with SVM: {accuracy}")

# Step 8: Save the model and vectorizer
joblib.dump(model, 'svm_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
