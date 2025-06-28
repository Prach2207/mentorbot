
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import sqlite3
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = 'secret_key'

# Initialize user DB
if not os.path.exists('users.db'):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

subject_tracker = {}

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash('Signup successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists.', 'danger')
        finally:
            conn.close()
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    answer, recommendation, question = "", "", ""
    if request.method == 'POST':
        question = request.form['question'].lower()
        answer = generate_answer(question)
        recommendation = generate_fake_recommendation(question)
        track_progress(question)

    total = sum(subject_tracker.values()) or 1
    subject_progress = {subj: int((count / total) * 100) for subj, count in subject_tracker.items()}

    return render_template('index.html',
                           username=session['username'],
                           answer=answer,
                           recommendation=recommendation,
                           subject_progress=subject_progress)

def generate_answer(question):
    try:
        # Try OpenAI first
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[Fallback triggered] OpenAI error: {e}")
        return fallback_answer(question)
def fallback_answer(q):
    q = q.lower()
    if "newton" in q and "second" in q:
        return "Newton's Second Law: Force = Mass × Acceleration (F = ma)."
    elif "newton" in q and "third" in q:
        return "Newton's Third Law: For every action, there is an equal and opposite reaction."
    elif "gravity" in q:
        return "Gravity is the force that attracts objects toward one another, especially towards the center of the Earth."
    elif "python" in q and "list" in q:
        return "In Python, a list is an ordered, changeable collection written using square brackets."
    elif "loop" in q:
        return "Loops allow you to repeat a block of code. Python supports for-loops and while-loops."
    else:
        return f"I'm still learning, but here’s what I know about '{q}': it’s a fascinating topic worth exploring!"



def generate_fake_recommendation(q):
    if "newton" in q:
        return "Watch: https://www.youtube.com/watch?v=kKKM8Y-u7ds (Newton's Laws of Motion)"
    elif "python" in q:
        return "Read: https://docs.python.org/3/tutorial/ (Official Python Tutorial)"
    else:
        return "Explore: https://www.khanacademy.org/ for deeper understanding."

def track_progress(q):
    keywords = {
        "newton": "science", "gravity": "science", "physics": "science",
        "python": "python", "loop": "python", "list": "python", "function": "python",
        "math": "math", "algebra": "math", "geometry": "math"
    }
    for key, subject in keywords.items():
        if key in q.lower():
            subject_tracker[subject] = subject_tracker.get(subject, 0) + 1


if __name__ == '__main__':
    app.run(debug=True)
