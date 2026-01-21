# Q3. Unique Visitors
# You receive visitor IDs (duplicates allowed):

# Tasks:
# Convert this into a set
# Print unique visitor count
# Add visitor 106
# Remove visitor 103

visitors = [101, 102, 103, 101, 104, 102, 105]

unique_visitors = set(visitors)

print(len(unique_visitors))

unique_visitors.add(106)
unique_visitors.remove(103)

print(unique_visitors)
