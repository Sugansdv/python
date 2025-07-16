# 13. Resume Skill Matcher
# Description: Match job profiles with resumes.
# Requirements:
# - {resume_id: {"skills": [...], "experience": ...}}
# - Search resumes with required skills
# - Filter by experience range
# - Use .values() and in for filtering

resumes = {
    1: {"skills": ["Python", "Django", "SQL"], "experience": 3},
    2: {"skills": ["JavaScript", "React", "Node.js"], "experience": 2},
    3: {"skills": ["Python", "Flask", "Machine Learning"], "experience": 4},
    4: {"skills": ["HTML", "CSS", "Bootstrap"], "experience": 1}
}

def match_by_skill(required_skill):
    print(f"\nResumes with skill: {required_skill}")
    for rid, data in resumes.items():
        if required_skill in data["skills"]:
            print(f"Resume {rid}: Skills = {data['skills']} | Experience = {data['experience']} yrs")

def filter_by_experience(min_exp, max_exp):
    print(f"\nResumes with experience between {min_exp} and {max_exp} years:")
    for rid, data in resumes.items():
        if min_exp <= data["experience"] <= max_exp:
            print(f"Resume {rid}: {data['skills']} | {data['experience']} yrs")

match_by_skill("Python")
match_by_skill("React")
filter_by_experience(2, 4)
