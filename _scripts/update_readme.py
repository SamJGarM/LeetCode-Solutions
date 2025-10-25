import os
from collections import Counter

REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPOSITORY_ROOT_PATH, "README.md")

EXTENSION_MAP = {
    ".py": "Python",
    ".c": "C",
    ".cpp": "C++",
    ".java": "Java",
    ".js": "JavaScript", 
}

def count_by_extension():
    counts = Counter()
    for _, _, files in os.walk(REPOSITORY_ROOT_PATH):
        for file in files:
            name, extension = os.path.splitext(file)
            if name.startswith("update_readme"):
                continue

            extension = extension.lower()

            if extension in EXTENSION_MAP:
                counts[EXTENSION_MAP[extension]] += 1

    return counts

def update_readme(counts):
    with open(README_PATH, "r") as file:
        lines = file.readlines()

    starting_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith("# Languages"):
            starting_line = i
            break

    if starting_line == None:
        raise ValueError("No languages section in README.md.")

    text = [
        "# Languages\n",
        "This repository currently holds solutions in the following languages:\n"
    ]

    for language, count in sorted(counts.items(), key = lambda x: x[1], reverse = True):
        text.append(f"- [{language}] - {count} Solutions\n")

    text.append("\n")

    ending_line = len(lines)
    for i in range(starting_line + 1, len(lines)):
        if lines[i].startswith("#") and i != starting_line:
            ending_line = i
            break

    updated_content = lines[:starting_line] + text + lines[ending_line:]

    with open(README_PATH, "w") as file:
        file.writelines(updated_content)

def main():
    counts = count_by_extension()
    update_readme(counts)

main()