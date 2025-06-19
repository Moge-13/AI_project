import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample dataset for training
data = {
    "description": [
        "There is a fire in the building",
        "A car accident happened on the main road",
        "A person is unconscious and needs medical help",
        "My house was robbed last night",
        "Someone is stuck in an elevator",
        "There is smoke coming from a factory",
        "A pedestrian was hit by a vehicle",
        "An elderly person fainted in the park",
        "I saw someone breaking into a store"
    ],
    "incident_type": ["fire", "accident", "medical", "theft", "rescue", "fire", "accident", "medical", "theft"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create TF-IDF Vectorizer & Naive Bayes Model Pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(df["description"], df["incident_type"])

# Save the trained model
joblib.dump(model, "incident_classifier.pkl")

print("✅ AI Model Trained and Saved Successfully!")
