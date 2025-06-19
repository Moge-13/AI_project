from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import sqlite3

app = Flask(__name__)
app.secret_key = "some-secret-key"

# Initialize Database
def init_db():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            incident_type TEXT,
            location TEXT,
            description TEXT,
            response TEXT
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# AI Response Generator
def generate_response(incident_type):
    responses = {
        "fire": "Emergency Alert: Fire department has been notified. Stay away from the fire and wait for firefighters.",
        "accident": "Emergency Alert: Paramedics and police have been dispatched. Please remain calm and assist if possible.",
        "medical": "Emergency Alert: An ambulance is on the way. Please provide first aid if trained.",
        "theft": "Emergency Alert: Police have been notified. Stay safe and do not engage the suspect."
    }
    return responses.get(incident_type.lower(), "Emergency Alert: Authorities have been notified.")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report", methods=["GET", "POST"])
def report_incident():
    if request.method == "POST":
        name = request.form.get("name")
        incident_type = request.form.get("incident_type")
        location = request.form.get("location")
        description = request.form.get("description")  # Using .get() to prevent KeyError

        # Validate that all fields are filled
        if not name or not incident_type or not location or not description:
            return "Error: All fields are required!", 400

        response_message = generate_response(incident_type)

        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO reports (name, incident_type, location, description, response) VALUES (?, ?, ?, ?, ?)",
                           (name, incident_type, location, description, response_message))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

        session["latest_report"] = {
            "name": name,
            "incident_type": incident_type,
            "location": location,
            "description": description,
            "response": response_message
        }
        return redirect(url_for("confirmation"))

    return render_template("report.html")

@app.route("/confirmation")
def confirmation():
    report_data = session.get("latest_report", None)
    return render_template("confirmation.html", report=report_data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)  # Correct Flask app initialization

@app.route('/report', methods=['POST'])
def report():
    try:
        # Check if the request content type is JSON
        if request.is_json:
            data = request.get_json()  # Retrieve JSON data from the request
            print(f"Received data: {data}")  # Debug: Print received data
            
            # Here you can process the data
            return jsonify({"message": "Report submitted successfully!"}), 200
        else:
            return jsonify({"error": "Expected JSON data"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Bad request"}), 400

if __name__ == '__main__':  # Corrected condition
    app.run(debug=True)
