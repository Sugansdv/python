import argparse
from resume.input import collect_input, load_input_from_json
from resume.template import format_resume_text, format_resume_markdown
from resume.export import export_resume

def main():
    parser = argparse.ArgumentParser(description="📄 Resume Formatter Generator")
    parser.add_argument("--input", help="Path to input JSON file")
    parser.add_argument("--format", choices=["txt", "md"], default="txt", help="Output format (txt/md)")
    parser.add_argument("--output", default="resume", help="Output filename (without extension)")
    args = parser.parse_args()

    if args.input:
        data = load_input_from_json(args.input)
    else:
        data = collect_input()

    if args.format == "md":
        content = format_resume_markdown(data)
    else:
        content = format_resume_text(data)

    export_resume(content, args.output, args.format)

if __name__ == "__main__":
    main()
