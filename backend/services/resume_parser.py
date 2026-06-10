import pdfplumber
import re

SKILL_KEYWORDS = [
    # Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "kotlin", "swift",
    "go", "rust", "php", "ruby", "scala", "r", "matlab", "bash",
    # Web
    "html", "css", "react", "angular", "vue", "node.js", "express", "django",
    "flask", "fastapi", "next.js", "tailwind", "bootstrap",
    # Data
    "pandas", "numpy", "tensorflow", "pytorch", "scikit-learn", "keras",
    "tableau", "power bi", "sql", "mysql", "postgresql", "mongodb", "redis",
    # Cloud/DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "github", "jenkins",
    "terraform", "ansible", "linux", "nginx",
    # Other
    "machine learning", "deep learning", "nlp", "computer vision", "rest api",
    "graphql", "microservices", "agile", "figma", "firebase", "flutter",
]

def extract_text_from_pdf(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []
    for skill in SKILL_KEYWORDS:
        # Use word boundary matching
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill.title())
    return list(set(found_skills))

def extract_name_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    lines = text.strip().split('\n')
    name = lines[0].strip() if lines else "User"
    return name, emails[0] if emails else ""