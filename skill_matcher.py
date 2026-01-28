def extract_skills(text,skills_db):
    found= set()
    for skill, keywords in skills_db.items():
        for kw in keywords:
            if kw in text:
                found.add(skill)
    return found

def calculate_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    return round((len(resume_skills & jd_skills)/ len(jd_skills)) * 100,2)
