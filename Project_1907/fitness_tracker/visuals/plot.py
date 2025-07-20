import matplotlib.pyplot as plt

def show_activity_chart(activities):
    if not activities:
        print("No data to show.")
        return

    types = {}
    for act in activities:
        types[act["type"]] = types.get(act["type"], 0) + act["duration"]

    labels = list(types.keys())
    values = list(types.values())

    plt.bar(labels, values, color="skyblue")
    plt.xlabel("Activity Type")
    plt.ylabel("Total Duration (mins)")
    plt.title("Activity Duration by Type")
    plt.tight_layout()
    plt.show()
