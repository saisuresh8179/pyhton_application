from flask import Flask, render_template, request, redirect, session
import mysql.connector
import secrets

secret_key = secrets.token_hex(16)  # Generates a 32-character random hexadecimal string

app = Flask(__name__)
app.secret_key = secret_key  # Replace with your own secret key

# MySQL configuration
db = mysql.connector.connect(
    host="database-1.cnaioemk4m2t.ap-south-1.rds.amazonaws.com",
    user="root",
    password="root1234",
    database="users_db"
)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        session['username'] = username
        return redirect('/dashboard')
    else:
        return "Invalid username or password"

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome, {session['username']}! This is your dashboard."
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')
    
@app.route('/health')
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
