# 20. Quiz Score Analyzer
# Goal: Record quiz attempts and analyze scores.
# Requirements:
# • Store data as (user_id, (quiz1, quiz2, quiz3))
# • Calculate best and worst scores.
# • Tuple slicing to get last 2 attempts.
# • Replace tuple after final submission.

# List of user quiz data
quiz_scores = [
    ("U001", (78, 85, 90)),
    ("U002", (65, 70, 60)),
    ("U003", (88, 92, 95)),
    ("U004", (50, 55, 58))
]

# Analyze scores
print(" Quiz Score Analysis:\n")
for user_id, scores in quiz_scores:
    best = max(scores)
    worst = min(scores)
    last_two = scores[-2:]
    print(f"User: {user_id}")
    print(f"  Scores     : {scores}")
    print(f"  Best Score : {best}")
    print(f"  Worst Score: {worst}")
    print(f"  Last 2     : {last_two}")
    print("-" * 30)

# Replace a user's scores after final submission (e.g., U002)
quiz_scores[1] = ("U002", (72, 80, 85))
print("\n Updated Scores for U002:")
print(quiz_scores[1])
