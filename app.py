from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong, random key

# In a real application, you would use a database for user management and questions.
users = {}
questions = [
    {
        'id': 1,
        'question': 'What is the capital of India?',
        'options': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai'],
        'correct_answer': 'Delhi'
    },
    {
        'id': 2,
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
        'correct_answer': 'Mars'
    },
    {
        'id': 3,
        'question': 'What is 2 + 2?',
        'options': ['3', '4', '5', '6'],
        'correct_answer': '4'
    }
]
results = {}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error='Username already exists', datetime=datetime)
        users[username] = {'password': password, 'results': []}  # Store results as a list
        return redirect(url_for('login'))
    return render_template('register.html', datetime=datetime)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))  # Redirect to dashboard after login
        else:
            return render_template('login.html', error='Invalid username or password', datetime=datetime)
    return render_template('login.html', datetime=datetime)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/exam', methods=['GET', 'POST'])
def exam():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_answers = {}
        for question in questions:
            answer = request.form.get(f'question_{question["id"]}')
            user_answers[question['id']] = answer

        score = 0
        for question in questions:
            if user_answers.get(question['id']) == question['correct_answer']:
                score += 1

        username = session['username']
        users[username]['results'].append({'score': score, 'total': len(questions), 'timestamp': datetime.now()})

        return redirect(url_for('result'))

    return render_template('exam.html', questions=questions, datetime=datetime)

@app.route('/result')
def result():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user_results = users[username]['results']
    if user_results:
        latest_result = user_results[-1]
        return render_template('result.html', result=latest_result, datetime=datetime)
    else:
        return render_template('result.html', message='No results available yet.', datetime=datetime)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user_results = users.get(username, {}).get('results', [])
    attempted_tests = len(user_results)
    total_tests_available = len(questions)

    average_score = 0
    if attempted_tests > 0:
        total_score = sum(result['score'] for result in user_results)
        average_score = total_score / attempted_tests

    return render_template('dashboard.html',
                           username=username,
                           total_tests=total_tests_available,
                           attempted_tests=attempted_tests,
                           average_score=average_score,
                           history=user_results,
                           datetime=datetime)

if __name__ == '__main__':
    app.run(debug=True)