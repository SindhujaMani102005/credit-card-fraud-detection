from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import random
import os
from utils.auth import oauth, login, authorize  # Import the OAuth logic

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "super_secret_key")  # Replace with secure key
oauth.init_app(app)

@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/simulate')
def simulate():
    return render_template('simulate.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Add your prediction logic here if needed
    return render_template('result.html', tables=[], titles=[])

@app.route('/start_simulation', methods=['POST'])
def start_simulation():
    interval = request.form['interval']
    flagged = [f"Transaction {i} flagged" for i in range(1, 4)]
    return render_template('simulate.html', flagged_transactions=flagged)

@app.route('/simulate/data')
def simulate_data():
    return jsonify({
        "timestamp": random.randint(1000, 9999),
        "fraud": random.randint(5, 20),
        "legit": random.randint(50, 150)
    })

# OAuth routes
@app.route('/login')
def login_route():
    return login()

@app.route('/auth')
def auth():
    return authorize()

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
