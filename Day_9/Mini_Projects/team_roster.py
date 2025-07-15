# 10. Sports Team Roster
# Goal: Store player data in a sports team.
# Requirements:
# • Store each player as: (player_id, name, (position, goals))
# • Display players with more than 10 goals.
# • Count how many strikers are in the team.
# • Use tuple packing and unpacking to build team summary.

# List of players
team = [
    (1, "Alex", ("Striker", 15)),
    (2, "Ben", ("Defender", 3)),
    (3, "Charlie", ("Midfielder", 8)),
    (4, "David", ("Striker", 12)),
    (5, "Ethan", ("Goalkeeper", 0)),
    (6, "Finn", ("Striker", 9))
]

# Display players with more than 10 goals
print(" Players with more than 10 goals:\n")
for player_id, name, (position, goals) in team:
    if goals > 10:
        print(f"{name} ({position}) - Goals: {goals}")

# Count number of strikers
striker_count = sum(1 for _, _, (position, _) in team if position == "Striker")
print(f"\n Total Strikers: {striker_count}")

# Build team summary using tuple packing and unpacking
print("\n Team Summary:\n")
for player in team:
    player_id, name, (position, goals) = player
    print(f"ID: {player_id}, Name: {name}, Position: {position}, Goals: {goals}")
