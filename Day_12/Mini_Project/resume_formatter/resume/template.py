def format_resume_text(data):
    lines = []
    lines.append(f"{data['name']}")
    lines.append(f"Email: {data['email']} | Phone: {data['phone']}")
    lines.append("\nSUMMARY:")
    lines.append(f"{data['summary']}\n")

    lines.append("SKILLS:")
    for skill in data['skills']:
        lines.append(f"- {skill.strip()}")
    
    lines.append("\nEXPERIENCE:")
    for exp in data['experience']:
        lines.append(f"{exp['title']} at {exp['company']} ({exp['years']})")
        lines.append(f"  {exp['description']}")
    
    lines.append("\nEDUCATION:")
    for edu in data['education']:
        lines.append(f"{edu['degree']} - {edu['institute']} ({edu['year']})")

    return "\n".join(lines)

def format_resume_markdown(data):
    lines = []
    lines.append(f"# {data['name']}")
    lines.append(f"**Email:** {data['email']}  \n**Phone:** {data['phone']}")
    lines.append(f"\n## Summary\n{data['summary']}\n")

    lines.append("## Skills")
    lines.append(", ".join(skill.strip() for skill in data['skills']))

    lines.append("\n## Experience")
    for exp in data['experience']:
        lines.append(f"### {exp['title']} - {exp['company']} ({exp['years']})")
        lines.append(f"{exp['description']}")

    lines.append("\n## Education")
    for edu in data['education']:
        lines.append(f"- **{edu['degree']}**, {edu['institute']} ({edu['year']})")

    return "\n".join(lines)
