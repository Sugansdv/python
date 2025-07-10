 #4. String Formatter Tool
# Accept user's name and salary as input
name = input("Enter your name: ")  
salary = input("Enter your salary (e.g., ₹50000): ") 

# Modify name using .title() 
formatted_name = name.title()

# Modify salary using .replace() 
numeric_salary = salary.replace("₹", "")  

# Convert salary string to float for formatting
salary_float = float(numeric_salary)

# Format string using % formatting
output = "My name is %s and I earn ₹%.2f" % (formatted_name, salary_float)

print(output)
