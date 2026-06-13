import os

with open('.env') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            key, val = line.split('=', 1)
            os.environ[key.strip()] = val.strip()

from flask import Flask, session
from extensions import mysql
import os
from dotenv import load_dotenv
import os

from flask import render_template

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('404.html'), 500

print("Templates path:", os.path.abspath('../frontend/templates'))

load_dotenv()

app = Flask(
    __name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)
app.config.from_object('config.Config')

mysql.init_app(app)

from routes.auth import auth_bp
from routes.resume import resume_bp
from routes.chatbot import chatbot_bp
from routes.report import report_bp

app.register_blueprint(auth_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(report_bp)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)