def add_activity(activities, date, type_, duration, calories):
    activities.append({
        "date": date,
        "type": type_,
        "duration": duration,
        "calories": calories
    })
    print("Activity added.")

def edit_activity(activities, date, new_type, new_duration, new_calories):
    for act in activities:
        if act["date"] == date:
            act["type"] = new_type
            act["duration"] = new_duration
            act["calories"] = new_calories
            print("Activity updated.")
            return
    print("Activity not found.")

def view_statistics(activities):
    if not activities:
        print("No data.")
        return

    grouped = {}
    total_calories = 0

    for act in activities:
        grouped.setdefault(act["type"], []).append(act)
        total_calories += act["calories"]

    print(f"Total Calories Burned: {total_calories}")
    print("Activities by Type:")
    for t, acts in grouped.items():
        total = sum(a["duration"] for a in acts)
        print(f"  {t}: {len(acts)} sessions, {total} mins")

    unique_types = {act["type"] for act in activities}
    print("Unique Activities:", ", ".join(unique_types))

    if total_calories > 2000:
        print("🎯 Great job! You’ve hit your calorie goal!")
    else:
        print("💡 Keep going! Set a goal for more activity.")
