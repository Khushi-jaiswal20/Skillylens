from flask import Blueprint, request, jsonify, session, render_template
from services.groq_service import chat_with_ai

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chatbot')
def chatbot_page():
    analysis = session.get('analysis', {})
    return render_template('chatbot.html', data=analysis)


@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    chat_history = data.get('history', [])
    
    analysis = session.get('analysis', {})
    job_role = analysis.get('job_role', 'Software Developer')
    level = analysis.get('level', 'Student')
    
    chat_history.append({"role": "user", "content": user_message})
    response = chat_with_ai(chat_history, job_role, level)
    
    # Save to DB only if logged in
    if 'user_id' in session:
        from extensions import mysql
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO chat_history 
            (user_id, job_role, message, response) VALUES (%s, %s, %s, %s)""",
            (session['user_id'], job_role, user_message, response))
        mysql.connection.commit()
    
    return jsonify({'response': response})