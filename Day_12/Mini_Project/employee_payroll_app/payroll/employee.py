from datetime import date

class Employee:
    def __init__(self, emp_id, name, designation, join_date):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.join_date = join_date  # YYYY-MM-DD format

    def get_experience(self):
        join = date.fromisoformat(self.join_date)
        today = date.today()
        return today.year - join.year - ((today.month, today.day) < (join.month, join.day))
