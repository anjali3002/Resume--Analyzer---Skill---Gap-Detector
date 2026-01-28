import streamlit as st

from resume_parser import extract_resume_text
from jd_parser import process_jd
from skill_matcher import extract_skills,calculate_score
from skills_db import SKILLS_DB


st.title('📝 Resume Analyzer & Skill Gap Detector ⚡')
resume_file = st.file_uploader('Upload Resume (PDF)', type=['pdf'])
jd_text = st.text_area('Paste Job Description')

if st.button('Analyze'):
    if resume_file and jd_text:
        resume_text = extract_resume_text(resume_file)
        jd_text = process_jd(jd_text)

        resume_skills = extract_skills(resume_text,SKILLS_DB)
        jd_skills = extract_skills(jd_text, SKILLS_DB)

        score = calculate_score(resume_skills, jd_skills)
        missing = jd_skills - resume_skills
        matched = resume_skills & jd_skills

        st.metric('Match Score',f"{score} %")
        st.success(f"Matched Skills: {','.join(matched)}")
        st.error(f"Missing Skills: {','.join(missing)}")
    else:
        st.warning('Please upload resume and paste JD')
