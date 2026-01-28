
# 📝 Resume Analyzer & Skill Gap Detector ⚡

A **Python + Streamlit application** that simulates an **ATS-style resume screening system**.  
It evaluates how well a candidate’s **PDF resume** matches a **job description**, returning a **matching score**, **matched skills**, and **missing skills**.

---

## 🚀 Why This Project?

Recruiters and job seekers need a fast way to assess resume–job fit.  
This project provides a **transparent, rule-based solution** that clearly explains *why* a resume matches or doesn’t.

---

## 🚀 Features

✅ Upload resume in **PDF format**  
✅ Paste **job description** text  
✅ Extract skills from resume and JD  
✅ Calculate **resume–job matching score (%)**  
✅ Display:
- ✔️ Matching skills  
- ❌ Missing skills (skill gaps)  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- PyPDF2  
- Regex & string matching 
- Git & GitHub  

---

## 📂 Project Structure

 ```bash
Resume_Analyzer/
│
├── app.py               # Streamlit application (UI & main logic)
├── resume_parser.py     # Extracts text & skills from resume PDF
├── jd_parser.py         # Parses and processes job description text
├── skill_matcher.py     # Compares resume skills with JD skills
├── skills_db.py         # Predefined skills database
│
├── .gitignore           # Ignores cache files & unnecessary files
└── README.md            # Project documentation






