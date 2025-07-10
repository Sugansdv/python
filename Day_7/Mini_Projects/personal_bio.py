#1. Personal Bio Generator
# Ask the user for name, age, job title
name = input("Enter your name: ")        
age = input("Enter your age: ")           
job = input("Enter your job title: ")    

# Clean extra spaces using .strip()
name = name.strip()
job = job.strip()

# Capitalize name using .upper()
name = name.upper()

# Display: "Hi, I'm JOHN. I'm 30 years old and I work as a Developer"
bio = f"Hi, I'm {name}. I'm {age} years old and I work as a {job}."
print(bio)

# Count total characters in the bio using len()
print("Total characters in bio:", len(bio))
