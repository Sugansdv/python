# 9. Hashtag Trend Tracker
# Goal: Track trending hashtags daily.
# Requirements:
# - Use daily sets of hashtags.
# - Combine all into a weekly trending set using update().
# - Find unique hashtags only used on one day.
# Concepts Covered: update(), symmetric_difference(), analysis.

monday = {"#mondaymotivation", "#work", "#coffee"}
tuesday = {"#coffee", "#productivity", "#meeting"}
wednesday = {"#wellness", "#work", "#coffee"}

weekly_trending = set()
weekly_trending.update(monday, tuesday, wednesday)

unique_one_day = monday ^ tuesday ^ wednesday

print("Weekly trending hashtags:", weekly_trending)
print("Hashtags used only on one day:", unique_one_day)
