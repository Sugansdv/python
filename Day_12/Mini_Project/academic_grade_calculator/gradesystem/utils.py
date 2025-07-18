def format_report(report):
    return f"""
    Report Card
    -----------
    Student: {report['student']}
    CGPA   : {report['CGPA']}
    Grade  : {report['Grade']}
    """
