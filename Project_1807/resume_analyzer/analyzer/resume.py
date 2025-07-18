
def extract_skills(resume_text):
    # Basic normalization and splitting
    words = resume_text.lower().replace(',', ' ').replace('.', ' ').split()
    
    # Sample skill keywords
    keywords = {
        "python", "java", "c++", "react", "node", "sql",
        "html", "css", "javascript", "machine", "learning",
        "data", "analysis", "excel", "django", "flask"
    }
    
    return set(words) & keywords

def add_resume(resumes, applicant_id, resume_text):
    skills = extract_skills(resume_text)
    resumes[applicant_id] = {
        "skills": skills
    }

def display_resumes(resumes):
    for aid, details in resumes.items():
        print(f"Applicant ID: {aid}")
        print(f"Skills Found: {', '.join(details['skills']) if details['skills'] else 'No relevant skills'}")
        print("-" * 30)
