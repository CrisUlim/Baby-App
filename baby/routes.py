from baby import app
from flask import render_template, redirect, url_for,  flash, request


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'admin@gmail.com' and password == '123456':
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
    return render_template('home_user.html')

@app.route('/history')
def history_page():
    heart_rate_data = [72, 74, 75, 78, 82, 80, 83, 85, 88, 90]
    oxygen_level_data = [97, 98, 98, 99, 99, 98, 97, 96, 95, 94]

    return render_template('history_user.html', heart_rate_data=heart_rate_data, oxygen_level_data=oxygen_level_data)
  

@app.route('/guide')
def guide_page():
    return render_template('guide_user.html')

@app.route('/account')
def account_page():
    
    return render_template('account_user.html')

@app.route("/logout")
def logout():
    return redirect(url_for('home_page'))

@app.route('/add_baby')
def add_baby():
    return render_template('add_baby.html')