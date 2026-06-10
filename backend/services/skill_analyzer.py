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