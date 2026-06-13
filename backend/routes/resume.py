from flask import Blueprint, request, jsonify, session, render_template
import os, json, re
from werkzeug.utils import secure_filename
from services.resume_parser import extract_text_from_pdf, extract_skills, extract_name_email, extract_projects
from services.skill_analyzer import analyze_skills, analyze_ats
from services.groq_service import generate_roadmap
from extensions import mysql
from data.skill_map import SKILL_MAP

resume_bp = Blueprint('resume', __name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@resume_bp.route('/upload', methods=['GET'])
def upload_page():
    if 'user_id' not in session:
        return render_template('upload.html', logged_in=False)
    return render_template('upload.html', logged_in=True)

@resume_bp.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['resume']
    job_role = request.form.get('job_role', 'Full Stack Developer')
    level = request.form.get('level', 'Student')

    if not allowed_file(file.filename):
        return jsonify({'error': 'Only PDF files allowed'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file.save(filepath)

    # Parse
    text = extract_text_from_pdf(filepath)
    extracted_skills   = extract_skills(text)
    extracted_projects = extract_projects(text)
    name, email        = extract_name_email(text)

    # Analyze
    analysis   = analyze_skills(extracted_skills, job_role, level)
    ats_result = analyze_ats(text)

    # Suggested projects from skill map
    role_data          = SKILL_MAP.get(job_role, {})
    suggested_projects = role_data.get('suggested_projects', [
        'Build a portfolio project using your top skills',
        'Contribute to an open-source project on GitHub',
        'Create a personal project solving a real problem',
    ])

    # Roadmap
    roadmap_raw = generate_roadmap(job_role, analysis['missing_skills'], level)
    try:
        json_match = re.search(r'\{.*\}', roadmap_raw, re.DOTALL)
        roadmap = json.loads(json_match.group()) if json_match else {}
    except:
        roadmap = {}

    result = {
        'name':               name,
        'job_role':           job_role,
        'level':              level,
        'existing_skills':    analysis['existing_skills'],
        'missing_skills':     analysis['missing_skills'],
        'readiness_score':    analysis['readiness_score'],
        'career_dna':         analysis['career_dna'],
        'ai_tools':           analysis['ai_tools'],
        'good_to_have':       analysis['good_to_have'],
        'roadmap':            roadmap,
        'ats_score':          ats_result['ats_score'],
        'ats_grade':          ats_result.get('ats_grade', ''),
        'is_ats_friendly':    ats_result['is_ats_friendly'],
        'ats_feedback':       ats_result['feedback'],
        'ats_tips':           ats_result['tips'],
        'extracted_projects': extracted_projects,
        'suggested_projects': suggested_projects,
    }

    # Save to DB if logged in
    if 'user_id' in session:
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO analyses
            (user_id, job_role, level, resume_text, existing_skills, missing_skills,
             readiness_score, roadmap, ai_tools, career_dna, ats_score, ats_feedback, good_to_have)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (
                session['user_id'], job_role, level, text[:5000],
                json.dumps(analysis['existing_skills']),
                json.dumps(analysis['missing_skills']),
                analysis['readiness_score'],
                json.dumps(roadmap),
                json.dumps(analysis['ai_tools']),
                json.dumps(analysis['career_dna']),
                ats_result['ats_score'],
                json.dumps(ats_result['feedback']),
                json.dumps(analysis['good_to_have'])
            ))
        mysql.connection.commit()
        session['analysis_id'] = cur.lastrowid

    session['analysis'] = result
    os.remove(filepath)
    return jsonify({'success': True, 'redirect': '/dashboard'})

@resume_bp.route('/dashboard')
def dashboard():
    analysis = session.get('analysis', {})
    if not analysis:
        return render_template('upload.html', error="Please upload your resume first")
    return render_template('dashboard.html', data=analysis)