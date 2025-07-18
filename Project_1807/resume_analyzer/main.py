
from analyzer.resume import add_resume, display_resumes

# Dictionary to hold applicant data
resume_data = {}

# Add resumes (simulate with text input)
add_resume(resume_data, ("A001",), "Experienced in Python, Java, and Machine Learning.")
add_resume(resume_data, ("A002",), "Skilled in React, Node.js, and HTML/CSS.")
add_resume(resume_data, ("A003",), "Familiar with C++, Excel, and data analysis.")

# Display extracted skills
display_resumes(resume_data)
