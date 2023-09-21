from baby import app
from flask import render_template, redirect, url_for, request, session, g
from baby.models import LoginSystem
import csv
from datetime import datetime


def read_csv_file(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if LoginSystem.query.filter_by(email=email, password=password).first():
            session['email'] = email
            return redirect(url_for('user_home'))
    return render_template('login.html')


@app.route('/forgot')
def reset_password():
    return render_template('forgot_pass.html')


@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/user')
def user_home():
    if g.email:
        file_path = '/home/cristian/Documents/Portofoliu/Baby/baby/temperatures.csv'
        extracted_data = read_csv_file(file_path)
        now = datetime.now()
        date = now.strftime("%d.%m.%Y, %H:%M")
        return render_template('home_user.html', email=session['email'],extracted_data=extracted_data, date=str(date))

    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.email = None

    if 'email' in session:
        g.email = session['email']


@app.route('/history')
def history_page():
    if g.email:
        file_path = '/home/cristian/Documents/Portofoliu/Baby/baby/data.csv'
        extracted_data = read_csv_file(file_path)

        return render_template('history_user.html', extracted_data=extracted_data,
                               email=session['email'])

    return redirect(url_for('login'))


@app.route('/guide')
def guide_page():
    if g.email:
        return render_template('guide_user.html', email=session['email'])

    return redirect(url_for('login'))


@app.route('/account')
def account_page():
    if g.email:
        return render_template('account_user.html', email=session['email'])

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('home_page'))


@app.route('/add_baby')
def add_baby():
    if g.email:
        return render_template('add_baby.html', email=session['email'])
    return redirect(url_for('login'))
