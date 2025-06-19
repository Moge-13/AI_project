#  AI-Powered Emergency Response System

This project is a web-based emergency reporting system that uses Artificial Intelligence to classify incidents based on the description provided by users. It automatically generates a response and stores all data securely in a local database.

---

## Features

- Simple and responsive web interface
- AI-based classification of incidents (Fire, Accident, Medical, Theft)
- Automatic response generation based on incident type
- Stores user reports in a SQLite database
- Confirmation page for user feedback

---

## Technologies Used

- Python
- Flask (Backend Framework)
- SQLite (Database)
- HTML, CSS, JavaScript (Frontend)
- Scikit-learn (AI model - Naive Bayes)
- Joblib (Model saving and loading)

---

---

##  How It Works

1. The user reports an incident by filling out a web form.
2. The system uses a pre-trained Naive Bayes model to classify the incident type.
3. An appropriate response message is generated automatically.
4. The incident details and response are saved into a SQLite database.
5. The user is shown a confirmation screen with the AI's response.

---
### step 1: Install Requirements
Make sure Python is installed, then run:
```bash
pip install flask pandas scikit-learn joblib

### Step 2: Train the AI Model

python train_model.py

This script trains a Naive Bayes model on sample data and saves it as incident_classifier.pkl.

Step 3: Run the Application

python app.py

Access the application at:
http://127.0.0.1:5000/
______________________________________
Future Improvements :

*Add voice input and location (Google Maps)

*Create admin panel to view all reports

*Enable report filtering and export to Excel

*Add user login & authentication
