from flask import Blueprint, request, session, redirect, render_template, jsonify
import bcrypt
from extensions import mysql

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return render_template('index.html')
@auth_bp.route('/about')
def about():
    return render_template('about.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, name, password FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        if user and bcrypt.checkpw(password.encode(), user[2].encode()):
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            return jsonify({'success': True})
        return jsonify({'error': 'Invalid credentials'}), 401
    return render_template('login.html')

@auth_bp.route('/check-login')
def check_login():
    return jsonify({'logged_in': 'user_id' in session})

@auth_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/login')
    
    cur = mysql.connection.cursor()
    
    # Get analyses
    cur.execute("""SELECT job_role, level, readiness_score, existing_skills, 
                   missing_skills, created_at FROM analyses 
                   WHERE user_id = %s ORDER BY created_at DESC LIMIT 5""",
                (session['user_id'],))
    analyses = cur.fetchall()
    
    # Get chat history
    cur.execute("""SELECT job_role, message, response, created_at 
                   FROM chat_history WHERE user_id = %s 
                   ORDER BY created_at DESC LIMIT 20""",
                (session['user_id'],))
    chats = cur.fetchall()
    
    return render_template('profile.html', 
                          analyses=analyses, 
                          chats=chats,
                          name=session.get('user_name'))

@auth_bp.route('/delete-account')
def delete_account():

    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']

    cur = mysql.connection.cursor()

    # delete analyses first
    cur.execute(
        "DELETE FROM analyses WHERE user_id=%s",
        (user_id,)
    )

    # delete chat history
    cur.execute(
        "DELETE FROM chat_history WHERE user_id=%s",
        (user_id,)
    )

    # now delete user
    cur.execute(
        "DELETE FROM users WHERE id=%s",
        (user_id,)
    )

    mysql.connection.commit()

    session.clear()

    return redirect('/')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = bcrypt.hashpw(data.get('password').encode(), bcrypt.gensalt()).decode()
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, password))
            mysql.connection.commit()
            return jsonify({'success': True})
        except:
            return jsonify({'error': 'Email already exists'}), 400
    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')