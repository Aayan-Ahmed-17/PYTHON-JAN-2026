# Q4. User Profile
# Create a dictionary for a user:
# Tasks:
# Print user name
# Update skill to "AI"
# Add key "country": "Pakistan"
# Loop and print all key-value pairs

user = {
    "name": "Aayan",
    "age": 20,
    "skill": "Python"
}
print(user["name"])

user["skill"] = "AI"

user.update({"country" : "Pakistan"})

for key, val in user.items():
    print(key, val)