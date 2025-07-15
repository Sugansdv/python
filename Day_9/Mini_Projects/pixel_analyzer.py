# 3. Image Pixel Color Analyzer
# Goal: Work with image pixel RGB color values.
# Requirements:
# • Store RGB values as (R, G, B) tuples.
# • Use a list of tuples to represent image pixels.
# • Count how many pixels match a specific color using .count().
# • Slice the pixel list to analyze a subregion.
# • Return dominant colors using tuple frequency.

from collections import Counter

# Simulated image data (a flat list of RGB pixel tuples)
pixels = [
    (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 0, 0), (0, 0, 255), (0, 0, 255), (0, 255, 0), (255, 255, 255),
    (0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 255, 0)
]

# Count specific color occurrences
target_color = (255, 0, 0)
count = pixels.count(target_color)
print(f"🔍 Pixels matching {target_color}: {count}")

# Slice the pixel list to analyze a subregion (e.g., first 10 pixels)
subregion = pixels[:10]
print("\n Subregion Pixels:")
for pixel in subregion:
    print(pixel)

# Return dominant colors using tuple frequency
color_counts = Counter(pixels)
most_common_colors = color_counts.most_common(3)

print("\n Top 3 Dominant Colors:")
for color, freq in most_common_colors:
    print(f"Color: {color}, Count: {freq}")
