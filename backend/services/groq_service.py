from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_roadmap(job_role, missing_skills, level):
    missing_str = ", ".join(missing_skills[:10])
    prompt = f"""You are a career mentor for tech students in India.
    
A {level} wants to become a {job_role}.
Their missing skills are: {missing_str}

Generate a structured 90-day learning roadmap with:
- Phase 1 (Days 1-30): Beginner foundations
- Phase 2 (Days 31-60): Intermediate skills  
- Phase 3 (Days 61-90): Advanced & projects

For each phase list 3-5 specific tasks with estimated hours.
Format as JSON with keys: phase1, phase2, phase3.
Each phase has: title, duration, tasks (array of: skill, task, hours, resource_name, resource_url)
Return ONLY valid JSON, no explanation."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.7
    )
    return response.choices[0].message.content

def chat_with_ai(messages, job_role, level):
    system_prompt = f"""You are SkillyLens AI — a smart career mentor for Indian tech students.
The user is a {level} targeting {job_role} role.
Give concise, practical, India-specific career advice.
Focus on: skills, placements, internships, resume tips, certifications, interview prep.
Keep responses under 150 words. Be encouraging and direct."""
    
    groq_messages = [{"role": "system", "content": system_prompt}]
    groq_messages.extend(messages)
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=groq_messages,
        max_tokens=300,
        temperature=0.8
    )
    return response.choices[0].message.content