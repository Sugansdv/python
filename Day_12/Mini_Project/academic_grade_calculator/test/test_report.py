from gradesystem.report import generate_report

def test_report_generation():
    report = generate_report("Test", {
        "Math": [90, 95, 85],
        "English": [80, 85, 90]
    })
    assert report["student"] == "Test"
    assert isinstance(report["CGPA"], float)
    assert report["Grade"] in ["A+", "A", "B", "C", "D", "F"]
