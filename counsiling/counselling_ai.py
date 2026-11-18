"""
College Course Selection Counselling AI
Run: python counselling_ai.py
Requires: Python 3.8+ (no third-party packages)

This is an educational, rule-based recommendation prototype, not an official
admissions eligibility checker. Confirm all requirements with the institution.
"""

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "courses.json")
RESULT_FILE = os.path.join(os.path.dirname(__file__), "counselling_result.json")


def load_courses():
    """Load course information from the JSON dataset."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("courses", [])
    except FileNotFoundError:
        raise SystemExit("Error: courses.json was not found. Keep it beside this Python file.")
    except json.JSONDecodeError:
        raise SystemExit("Error: courses.json contains invalid JSON.")


def ask_float(prompt, minimum=0, maximum=100000000):
    while True:
        try:
            value = float(input(prompt).strip())
            if minimum <= value <= maximum:
                return value
            print(f"Enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("Please enter a valid number.")


def get_student_details():
    print("\n=== Student Information ===")
    name = input("Student name: ").strip() or "Student"
    marks = ask_float("Class 12 percentage (0-100): ", 0, 100)
    budget = ask_float("Maximum annual tuition budget (in INR): ", 0, 100000000)
    print("\nEnter interests separated by commas.")
    print("Examples: computers, programming, business, biology, writing")
    interests = {
        item.strip().lower()
        for item in input("Your interests: ").split(",")
        if item.strip()
    }
    career_goal = input("Preferred career (optional): ").strip().lower()
    preferred_stream = input(
        "Preferred stream (optional: Engineering, Commerce, Science, Management, "
        "Health Sciences, Arts and Humanities): "
    ).strip().lower()

    return {
        "name": name,
        "class_12_percentage": marks,
        "annual_budget_inr": budget,
        "interests": sorted(interests),
        "career_goal": career_goal,
        "preferred_stream": preferred_stream
    }


def score_course(student, course):
    """
    Score a course using transparent matching rules:
    50 points for interest overlap, 25 for academic eligibility,
    15 for budget fit, and 10 for preferred stream.
    """
    student_interests = set(student["interests"])
    course_interests = {word.lower() for word in course.get("interests", [])}

    overlap = student_interests.intersection(course_interests)
    interest_score = min(50, len(overlap) * 15)

    meets_marks = student["class_12_percentage"] >= course["minimum_percentage"]
    eligibility_score = 25 if meets_marks else 0

    fee = course["estimated_annual_fee"]
    budget = student["annual_budget_inr"]
    if budget <= 0:
        budget_score = 0
    elif fee <= budget:
        budget_score = 15
    else:
        # Partial credit when the estimated fee is close to the student's budget.
        budget_score = max(0, 15 * budget / fee)

    preferred = student["preferred_stream"]
    stream_score = 10 if preferred and preferred == course["stream"].lower() else 0

    total = round(interest_score + eligibility_score + budget_score + stream_score, 1)

    career_match = False
    if student["career_goal"]:
        career_match = any(
            student["career_goal"] in career.lower()
            for career in course.get("career_paths", [])
        )
        if career_match:
            total = min(100, total + 10)

    return {
        "score": round(total, 1),
        "interest_matches": sorted(overlap),
        "meets_sample_marks_cutoff": meets_marks,
        "estimated_annual_fee": fee,
        "within_budget": fee <= budget if budget > 0 else None,
        "career_match": career_match
    }


def recommend_courses(student, courses):
    results = []
    for course in courses:
        details = score_course(student, course)
        results.append({
            "course_id": course["id"],
            "course_name": course["name"],
            "stream": course["stream"],
            "description": course["description"],
            "career_paths": course["career_paths"],
            "typical_subjects": course["typical_subjects"],
            "minimum_percentage_in_sample_data": course["minimum_percentage"],
            **details
        })

    # Put courses meeting the sample marks threshold first, then rank by score.
    results.sort(
        key=lambda item: (item["meets_sample_marks_cutoff"], item["score"]),
        reverse=True
    )
    return results


def display_results(student, recommendations):
    print(f"\n=== Counselling Results for {student['name']} ===")
    if not recommendations:
        print("No courses are available in the dataset.")
        return

    for index, item in enumerate(recommendations[:5], start=1):
        print(f"\n{index}. {item['course_name']} ({item['course_id']})")
        print(f"   Match score: {item['score']}/100")
        print(f"   Stream: {item['stream']}")
        print(f"   Estimated annual fee: INR {item['estimated_annual_fee']:,.0f}")
        print(f"   Meets sample marks cutoff: {'Yes' if item['meets_sample_marks_cutoff'] else 'No'}")
        print(f"   Interest matches: {', '.join(item['interest_matches']) or 'None'}")
        print(f"   Career paths: {', '.join(item['career_paths'])}")
        print(f"   Why consider it: {item['description']}")

    print("\nImportant: Match scores are guidance, not admission guarantees.")
    print("Check subject prerequisites, entrance exams, reservation rules,")
    print("accreditation, current fees and official cutoffs with each college.")


def save_results(student, recommendations):
    output = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "student": student,
        "recommendations": recommendations[:5],
        "disclaimer": (
            "Educational guidance only. Sample cutoffs and fees are illustrative; "
            "verify current official admission requirements with each institution."
        )
    }
    with open(RESULT_FILE, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4, ensure_ascii=False)
    print(f"\nYour counselling report was saved to: {RESULT_FILE}")


def main():
    courses = load_courses()
    student = get_student_details()
    recommendations = recommend_courses(student, courses)
    display_results(student, recommendations)
    save_results(student, recommendations)


if __name__ == "__main__":
    main()
