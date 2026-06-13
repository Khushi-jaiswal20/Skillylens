# 🚀 SkillyLens – "See the Gap, Bridge the Path"

SkillyLens is an AI-powered career guidance platform designed to help students and graduates evaluate their career readiness, identify skill gaps, improve ATS compatibility, and receive personalized learning roadmaps.

The platform analyzes resumes, generates career insights, evaluates ATS friendliness, recommends AI tools, and provides an AI mentor for career guidance.

---

## ✨ Features

### 📄 Resume Analysis

* Upload PDF resumes
* Automatic skill extraction
* Role-based skill matching
* Existing vs Missing Skills detection
* Career Readiness Score calculation

### 🧬 Career DNA Report

Visual analysis across multiple dimensions:

* Technical Skills
* Skill Breadth
* Role Alignment
* AI Readiness
* Future Growth Potential

### 🎯 Skill Gap Analysis

* Compare resume skills with industry requirements
* Identify missing skills for target roles
* Highlight additional good-to-have skills

### 📊 ATS Resume Checker

Evaluates whether a resume is ATS-friendly.

Includes:

* ATS Compatibility Score
* ATS Friendly / Not Friendly Status
* Resume Length Analysis
* Contact Information Validation
* Section Header Detection
* Action Verb Analysis
* Quantified Achievement Detection
* ATS Formatting Checks
* Personalized Improvement Tips

### 🗺 Personalized 90-Day Learning Roadmap

AI-generated roadmap including:

* Beginner Foundations
* Intermediate Skill Building
* Advanced Projects
* Curated Learning Resources

### 🤖 AI Tools Recommendation

Curated AI tools for each role:

* Popular industry tools
* Underrated productivity tools
* Learning and development resources

### 💬 Skilly Mentor

Interactive chatbot powered by Groq LLaMA:

* Career guidance
* Skill recommendations
* Interview preparation support
* Industry-specific advice

### 👤 User Profiles

* Secure Authentication
* Analysis History
* Chat History
* Profile Management
* Account Deletion Support

### 📑 PDF Report Generation

Download complete Career DNA reports including:

* Readiness Score
* Skill Analysis
* ATS Evaluation
* Learning Roadmap

---

## ⚙ How It Works

1. **Upload Resume**

   * Upload your PDF resume.

2. **Select Target Role and Current Level**

   * Choose your target job role and current education level.

3. **Resume Analysis**

   * Skills are extracted and compared against industry requirements.

4. **ATS Evaluation**

   * The resume is checked for ATS compatibility and improvement areas.

5. **Career DNA Generation**

   * Readiness score, skill gaps, and career insights are generated.

6. **Personalized Roadmap**

   * A 90-day learning roadmap is created based on missing skills.

7. **Skilly Mentor Support**

   * Users can interact with the AI mentor for career guidance and recommendations.

---

## 🛠 Tech Stack

### Backend & Database

* Python (Flask)
* MySQL
* Flask-MySQLdb

### AI & Processing

* Groq API (LLaMA Models)
* PDFPlumber
* Regular Expressions (NLP-based extraction)

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Report Generation

* ReportLab

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```bash
SkillyLens/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── data/
│   ├── uploads/
|   ├── config.py
|   ├── extentions.py
│   └── app.py
|   
│
├── frontend/
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/skillylens.git
cd skillylens
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
MYSQL_HOST=localhost
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DB=skillylens

GROQ_API_KEY=your_groq_api_key
```

### 6. Run Application

```bash
python app.py
```

Open:

```bash
http://127.0.0.1:5000
```

---

## 🎯 Future Enhancements

* AI Mock Interview Simulator
* LinkedIn Profile Analyzer
* Resume vs Job Description Matching
* Internship & Job Recommendation System
* Machine Learning Based Personalized Career Recommendations
* Company-Specific Preparation Roadmaps

---

## 👩‍💻 Team

### ForeTech

Built as a project to help students navigate their career journey using AI-powered insights.

---

## 📜 License

This project is developed for educational and portfolio purposes.