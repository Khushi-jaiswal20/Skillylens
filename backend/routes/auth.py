from flask import Blueprint, request, session, redirect, render_template, jsonify
import bcrypt
from extensions import mysql
import json

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
    cur.execute("""SELECT id, job_role, level, readiness_score, existing_skills, 
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

@auth_bp.route('/profile/analysis/<int:analysis_id>')
def view_analysis(analysis_id):
    if 'user_id' not in session:
        return redirect('/login')
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM analyses WHERE id = %s AND user_id = %s""",
                (analysis_id, session['user_id']))
    row = cur.fetchone()
    for i, val in enumerate(row):
        print(i, type(val), val)
    if not row:
        return "Not found", 404
    for i, value in enumerate(row):
     print(i, type(value), value)
    
    # Reconstruct analysis data
    data = {
    'job_role': row[2],
    'level': row[3],

    'existing_skills': json.loads(row[5] or '[]'),
    'missing_skills': json.loads(row[6] or '[]'),

    'readiness_score': row[7],

    'roadmap': json.loads(row[8] or '{}'),
    'ai_tools': json.loads(row[9] or '{}'),

    'good_to_have': json.loads(row[11] or '[]'),
    'career_dna': json.loads(row[12] or '{}'),

    'ats_score': row[13] or 0,
    'ats_feedback': json.loads(row[14] or '[]'),

    'name': session.get('user_name', '')
}
    session['analysis'] = data
    return render_template('dashboard.html', data=data)

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

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')