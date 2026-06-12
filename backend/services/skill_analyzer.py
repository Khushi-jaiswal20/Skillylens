from data.skill_map import get_skills_for_role

def analyze_skills(extracted_skills, job_role, level):
    role_data = get_skills_for_role(job_role)
    required = [s.lower() for s in role_data.get("required", [])]
    extracted_lower = [s.lower() for s in extracted_skills]
    
    existing = [s for s in required if s in extracted_lower]
    missing = [s for s in required if s not in extracted_lower]
    
    readiness_score = round((len(existing) / len(required)) * 100, 1) if required else 0
    
    # Level-based bonus
    level_bonus = {"Student": 0, "Final-Year Student": 5, "Graduate": 10}
    readiness_score = min(100, readiness_score + level_bonus.get(level, 0))
    
    # Career DNA axes
    tech_skills = ["python", "java", "javascript", "sql", "docker", "git", "react"]
    soft_skills_keywords = ["communication", "leadership", "teamwork", "management"]
    
    tech_score = round(sum(1 for s in tech_skills if s in extracted_lower) / len(tech_skills) * 100)
    ai_tools = role_data.get("ai_tools", {})
    
    career_dna = {
        "Technical Skills": tech_score,
        "Skill Breadth": min(100, len(extracted_skills) * 5),
        "Role Alignment": readiness_score,
        "AI Readiness": min(100, len(ai_tools.get("underrated", [])) * 15 + 20),
        "Future Score": min(100, readiness_score * 0.6 + len(extracted_skills) * 2)
    }
    
    return {
        "existing_skills": existing,
        "missing_skills": missing,
        "readiness_score": readiness_score,
        "career_dna": career_dna,
        "ai_tools": ai_tools,
        "good_to_have": role_data.get("good_to_have", [])
    }
def analyze_ats(text):
    score = 0
    feedback = []
    tips = []

    # 1. Length check
    word_count = len(text.split())
    if 300 <= word_count <= 800:
        score += 15
        feedback.append({"check": "Resume Length", "status": "pass", "msg": f"{word_count} words — ideal range"})
    else:
        feedback.append({"check": "Resume Length", "status": "fail",
                        "msg": f"{word_count} words — {'too short' if word_count < 300 else 'too long'}. Keep 300-800 words."})
        tips.append("Trim your resume to 300-800 words for ATS parsing.")

    # 2. Contact info
    import re
    has_email = bool(re.search(r'[\w.]+@[\w.]+\.\w+', text))
    has_phone = bool(re.search(r'[\+]?[\d\s\-]{10,}', text))
    if has_email and has_phone:
        score += 15
        feedback.append({"check": "Contact Information", "status": "pass", "msg": "Email & phone found"})
    else:
        missing = []
        if not has_email: missing.append("email")
        if not has_phone: missing.append("phone")
        feedback.append({"check": "Contact Information", "status": "fail",
                        "msg": f"Missing: {', '.join(missing)}"})
        tips.append(f"Add your {' and '.join(missing)} at the top of your resume.")

    # 3. Section headers
    sections = ['experience', 'education', 'skills', 'projects', 'summary', 'objective', 'certifications']
    text_lower = text.lower()
    found_sections = [s for s in sections if s in text_lower]
    if len(found_sections) >= 4:
        score += 20
        feedback.append({"check": "Section Headers", "status": "pass",
                        "msg": f"Found: {', '.join(found_sections)}"})
    else:
        feedback.append({"check": "Section Headers", "status": "warn",
                        "msg": f"Only found: {', '.join(found_sections) or 'none'}. Add standard section headers."})
        tips.append("Use standard headers: Experience, Education, Skills, Projects, Summary.")

    # 4. Bullet points / action verbs
    action_verbs = ['developed', 'built', 'designed', 'implemented', 'led', 'created',
                    'managed', 'improved', 'reduced', 'increased', 'deployed', 'automated']
    found_verbs = [v for v in action_verbs if v in text_lower]
    if len(found_verbs) >= 4:
        score += 20
        feedback.append({"check": "Action Verbs", "status": "pass",
                        "msg": f"Strong verbs found: {', '.join(found_verbs[:5])}"})
    else:
        feedback.append({"check": "Action Verbs", "status": "warn",
                        "msg": "Use more action verbs to describe your experience."})
        tips.append("Start bullet points with: Developed, Built, Designed, Implemented, Led, Automated.")

    # 5. Quantifiable achievements
    numbers = re.findall(r'\d+[%+]?', text)
    if len(numbers) >= 3:
        score += 15
        feedback.append({"check": "Quantified Achievements", "status": "pass",
                        "msg": f"{len(numbers)} numbers/metrics found — great!"})
    else:
        feedback.append({"check": "Quantified Achievements", "status": "fail",
                        "msg": "Add numbers/metrics to your achievements."})
        tips.append("Quantify impact: 'Improved performance by 40%', 'Built app with 1000+ users'.")

    # 6. No tables/columns check (heuristic)
    if '|' not in text and '\t\t' not in text:
        score += 15
        feedback.append({"check": "ATS-Safe Formatting", "status": "pass",
                        "msg": "No tables/columns detected — ATS friendly!"})
    else:
        feedback.append({"check": "ATS-Safe Formatting", "status": "fail",
                        "msg": "Tables or columns detected — ATS may misread."})
        tips.append("Avoid tables, columns, text boxes. Use simple single-column layout.")

    # Final verdict
    is_ats_friendly = score >= 60
    return {
        "ats_score": score,
        "is_ats_friendly": is_ats_friendly,
        "feedback": feedback,
        "tips": tips
    }