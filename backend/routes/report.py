from flask import Blueprint, session, send_file
from services.pdf_generator import generate_pdf_report
import os

report_bp = Blueprint('report', __name__)

@report_bp.route('/download-report')
def download_report():
    analysis = session.get('analysis', {})
    if not analysis:
        return "No analysis found", 404
    filepath = generate_pdf_report(analysis)
    return send_file(filepath, as_attachment=True, download_name='SkillyLens_Report.pdf')

from flask import Blueprint, session, send_file, jsonify

report_bp = Blueprint('report', __name__)

@report_bp.route('/download-report')
def download_report():
    # Login check
    if 'user_id' not in session:
        return jsonify({'error': 'login_required'}), 401
    
    analysis = session.get('analysis', {})
    if not analysis:
        return "No analysis found", 404
    
    from services.pdf_generator import generate_pdf_report
    filepath = generate_pdf_report(analysis)
    return send_file(filepath, as_attachment=True, download_name='SkillyLens_Report.pdf')