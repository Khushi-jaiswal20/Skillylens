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
    text_lower = text.lower()
    import re

    # ── CHECK 1: Word Count (weight: 15) ──
    word_count = len(text.split())
    if 300 <= word_count <= 700:
        score += 15
        feedback.append({
            "check": "Resume Length",
            "status": "pass",
            "msg": f"{word_count} words — ideal range (300–700)",
            "weight": 15, "earned": 15
        })
    elif 200 <= word_count < 300 or 700 < word_count <= 900:
        score += 8
        feedback.append({
            "check": "Resume Length",
            "status": "warn",
            "msg": f"{word_count} words — slightly {'short' if word_count < 300 else 'long'}. Aim for 300–700.",
            "weight": 15, "earned": 8
        })
    else:
        feedback.append({
            "check": "Resume Length",
            "status": "fail",
            "msg": f"{word_count} words — {'too short' if word_count < 200 else 'too long'}. Keep 300–700 words.",
            "weight": 15, "earned": 0
        })
        tips.append("Trim your resume to 300–700 words. ATS systems prefer concise, scannable content.")

    # ── CHECK 2: Contact Info (weight: 15) ──
    has_email = bool(re.search(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}', text))
    has_phone = bool(re.search(r'[\+]?[\d\s\(\)\-]{10,15}', text))
    has_linkedin = 'linkedin' in text_lower
    contact_earned = (8 if has_email else 0) + (7 if has_phone else 0)
    score += contact_earned
    if has_email and has_phone:
        feedback.append({
            "check": "Contact Information",
            "status": "pass",
            "msg": f"Email ✓  Phone ✓  {'LinkedIn ✓' if has_linkedin else 'LinkedIn not found — add it'}",
            "weight": 15, "earned": contact_earned
        })
    else:
        missing = []
        if not has_email: missing.append("email")
        if not has_phone: missing.append("phone number")
        feedback.append({
            "check": "Contact Information",
            "status": "fail",
            "msg": f"Missing: {', '.join(missing)}",
            "weight": 15, "earned": contact_earned
        })
        tips.append(f"Add your {' and '.join(missing)} clearly at the top of your resume.")

    # ── CHECK 3: Section Headers (weight: 20) ──
    required_sections = ['experience', 'education', 'skills']
    optional_sections = ['projects', 'summary', 'objective', 'certifications',
                         'achievements', 'internship', 'publications']
    found_required = [s for s in required_sections if s in text_lower]
    found_optional = [s for s in optional_sections if s in text_lower]
    all_found = found_required + found_optional

    if len(found_required) == 3:
        section_earned = min(20, 12 + len(found_optional) * 2)
        score += section_earned
        feedback.append({
            "check": "Section Headers",
            "status": "pass",
            "msg": f"Found: {', '.join(all_found[:5])}{'...' if len(all_found) > 5 else ''}",
            "weight": 20, "earned": section_earned
        })
    elif len(found_required) >= 2:
        score += 10
        missing_req = [s for s in required_sections if s not in text_lower]
        feedback.append({
            "check": "Section Headers",
            "status": "warn",
            "msg": f"Missing required sections: {', '.join(missing_req)}",
            "weight": 20, "earned": 10
        })
        tips.append(f"Add these standard section headers: {', '.join(missing_req).title()}")
    else:
        feedback.append({
            "check": "Section Headers",
            "status": "fail",
            "msg": "Critical sections missing. ATS cannot parse your resume properly.",
            "weight": 20, "earned": 0
        })
        tips.append("Add these headers: Experience, Education, Skills, Projects. ATS systems look for exact keywords.")

    # ── CHECK 4: Action Verbs (weight: 20) ──
    action_verbs = [
        'developed', 'built', 'designed', 'implemented', 'led', 'created',
        'managed', 'improved', 'reduced', 'increased', 'deployed', 'automated',
        'optimized', 'architected', 'integrated', 'delivered', 'launched',
        'collaborated', 'mentored', 'analyzed', 'engineered', 'established'
    ]
    found_verbs = [v for v in action_verbs if v in text_lower]
    if len(found_verbs) >= 6:
        score += 20
        feedback.append({
            "check": "Action Verbs",
            "status": "pass",
            "msg": f"Strong verbs found ({len(found_verbs)}): {', '.join(found_verbs[:5])}…",
            "weight": 20, "earned": 20
        })
    elif len(found_verbs) >= 3:
        score += 12
        feedback.append({
            "check": "Action Verbs",
            "status": "warn",
            "msg": f"Only {len(found_verbs)} action verbs found. Need 6+ for strong ATS score.",
            "weight": 20, "earned": 12
        })
        tips.append("Use more action verbs: Developed, Built, Implemented, Optimized, Deployed, Led.")
    else:
        feedback.append({
            "check": "Action Verbs",
            "status": "fail",
            "msg": "Very few action verbs. Your experience descriptions are too passive.",
            "weight": 20, "earned": 0
        })
        tips.append("Start every bullet point with an action verb. Example: 'Developed a REST API that handled 10K+ requests/day'")

    # ── CHECK 5: Quantified Achievements (weight: 15) ──
    metrics = re.findall(r'\d+\s*[%+xX]|\d+\s*(users|requests|projects|hours|days|weeks|'
                         r'months|clients|members|lines|commits|apps|features|bugs)', text_lower)
    plain_numbers = re.findall(r'\b\d{2,}\b', text)  # 2+ digit numbers
    total_metrics = len(metrics) + min(3, len(plain_numbers) // 3)

    if total_metrics >= 4:
        score += 15
        feedback.append({
            "check": "Quantified Achievements",
            "status": "pass",
            "msg": f"{total_metrics} measurable results found — excellent!",
            "weight": 15, "earned": 15
        })
    elif total_metrics >= 2:
        score += 8
        feedback.append({
            "check": "Quantified Achievements",
            "status": "warn",
            "msg": f"Only {total_metrics} metrics found. Add more numbers to strengthen impact.",
            "weight": 15, "earned": 8
        })
        tips.append("Quantify your impact: '40% performance improvement', 'Built app with 500+ users', 'Reduced load time by 2s'")
    else:
        feedback.append({
            "check": "Quantified Achievements",
            "status": "fail",
            "msg": "No measurable results found. Numbers make your resume 3x more impactful.",
            "weight": 15, "earned": 0
        })
        tips.append("Add numbers everywhere possible. Even estimates work: '~500 lines of code', '3 team members led'.")

    # ── CHECK 6: ATS-Safe Formatting (weight: 15) ──
    has_tables = text.count('|') >= 3
    has_special_chars = len(re.findall(r'[★●◆▸►✓✗]', text)) > 5
    file_safe = not has_tables and not has_special_chars

    if file_safe:
        score += 15
        feedback.append({
            "check": "ATS-Safe Formatting",
            "status": "pass",
            "msg": "No tables or special characters detected — clean and ATS parseable.",
            "weight": 15, "earned": 15
        })
    elif has_tables and has_special_chars:
        feedback.append({
            "check": "ATS-Safe Formatting",
            "status": "fail",
            "msg": "Tables and special characters detected — ATS may completely misread your resume.",
            "weight": 15, "earned": 0
        })
        tips.append("Remove all tables, text boxes, and special bullet symbols (★, ●, ◆). Use simple hyphens ( - ) instead.")
    else:
        score += 7
        issue = "tables" if has_tables else "special characters"
        feedback.append({
            "check": "ATS-Safe Formatting",
            "status": "warn",
            "msg": f"Detected {issue} that may confuse ATS parsers.",
            "weight": 15, "earned": 7
        })
        tips.append(f"Remove {issue} from your resume for better ATS compatibility.")

    score = min(100, score)
    is_ats_friendly = score >= 60

    # Grade
    if score >= 85:
        grade = "A — Excellent"
    elif score >= 70:
        grade = "B — Good"
    elif score >= 55:
        grade = "C — Average"
    elif score >= 40:
        grade = "D — Needs Work"
    else:
        grade = "F — Poor"

    return {
        "ats_score": score,
        "ats_grade": grade,
        "is_ats_friendly": is_ats_friendly,
        "feedback": feedback,
        "tips": tips
    }