# AI Career Guidance System (Rule-Based Expert System)

def get_user_input():
    print("\nAnswer with y (yes) or n (no)\n")

    skills = {
        "programming": input("Do you like programming? (y/n): ").lower(),
        "math": input("Are you good at mathematics/statistics? (y/n): ").lower(),
        "design": input("Do you like design & creativity? (y/n): ").lower(),
        "security": input("Are you interested in cyber security? (y/n): ").lower(),
        "data": input("Do you like working with data? (y/n): ").lower()
    }
    return skills


def evaluate_career(skills):
    scores = {
        "AI Engineer": 0,
        "Data Scientist": 0,
        "Web Developer": 0,
        "Cyber Security Analyst": 0
    }

    # Rule-based scoring
    if skills["programming"] == 'y':
        scores["AI Engineer"] += 2
        scores["Web Developer"] += 2
        scores["Cyber Security Analyst"] += 1

    if skills["math"] == 'y':
        scores["AI Engineer"] += 2
        scores["Data Scientist"] += 3

    if skills["data"] == 'y':
        scores["Data Scientist"] += 3
        scores["AI Engineer"] += 1

    if skills["design"] == 'y':
        scores["Web Developer"] += 3

    if skills["security"] == 'y':
        scores["Cyber Security Analyst"] += 4

    return scores


def suggest_career(scores):
    best_career = max(scores, key=scores.get)
    return best_career


def main():
    print("🎓 AI Career Guidance System")
    print("-----------------------------")

    user_skills = get_user_input()
    career_scores = evaluate_career(user_skills)
    result = suggest_career(career_scores)

    print("\n📊 Career Scores:")
    for career, score in career_scores.items():
        print(f"{career}: {score}")

    print("\n✅ Recommended Career Path:")
    print(f"👉 {result}")


if __name__ == "__main__":
    main()