with open("story.txt", "r") as f:
    story = f.read()
import re
placeholders = set(re.findall(r"<(.*?)>", story))
answers = {}
for placeholder in placeholders:
    user_input = input(f"ENter a word for '{placeholder}': ")
    answers[placeholder] = user_input
for key, value in answers.items():
    story = story.replace(f"<{key}>", value)

print("\nYour story:")
print(story)
