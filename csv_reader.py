import csv
import sys
import os


GRADE_THRESHOLDS = {
    "A+": 90,
    "A":  85,
    "A-": 80,
    "B+": 77,
    "B":  73,
    "Pass": 50,
}


def parse_row(row):
    """Parse a CSV row into course name, exam weight, bonus, and list of marks.

    Format: [Name (optional)], Exam Weight, Bonus, Mark1, Mark2, ...
    If the first field is not a number, it is treated as the course name.
    """
    if not row or all(cell.strip() == "" for cell in row):
        return None

    idx = 0
    course_name = None

    # Check if first field is a course name (non-numeric)
    first = row[0].strip()
    try:
        float(first)
    except ValueError:
        # Not a number — treat as course name
        course_name = first if first else None
        idx = 1

    # Exam weight
    if idx >= len(row):
        return None
    exam_weight = float(row[idx].strip())
    idx += 1

    # Bonus (0 if empty)
    bonus = 0.0
    if idx < len(row):
        bonus_str = row[idx].strip()
        bonus = float(bonus_str) if bonus_str else 0.0
        idx += 1

    # Remaining fields are individual marks (course % earned)
    marks = []
    for cell in row[idx:]:
        val = cell.strip()
        if val:
            marks.append(float(val))

    return {
        "name": course_name,
        "exam_weight": exam_weight,
        "bonus": bonus,
        "marks": marks,
    }


def compute_results(course):
    """Compute marks gained, marks lost, and required exam scores."""
    exam_weight = course["exam_weight"]
    bonus = course["bonus"]
    marks = course["marks"]

    pre_exam_weight = 100 - exam_weight
    marks_gained = sum(marks)
    marks_lost = pre_exam_weight - marks_gained

    results = {}
    for grade, threshold in GRADE_THRESHOLDS.items():
        needed = (threshold - marks_gained - bonus) / exam_weight * 100
        results[grade] = round(needed, 2)

    return {
        "pre_exam_weight": pre_exam_weight,
        "marks_gained": marks_gained,
        "marks_lost": round(marks_lost, 2),
        "bonus": bonus,
        "exam_weight": exam_weight,
        "grades": results,
    }


def format_course(course, results):
    """Format the output for a single course."""
    lines = []

    header = f"For {course['name']}:" if course["name"] else "Results:"
    lines.append(header)
    lines.append("")
    lines.append(f"  Pre-exam weight: {results['pre_exam_weight']}%")
    lines.append(f"  Marks gained:    {results['marks_gained']}%")
    lines.append(f"  Marks lost:      {results['marks_lost']}%")
    if results["bonus"] > 0:
        lines.append(f"  Bonus:           {results['bonus']}%")
    lines.append(f"  Exam weight:     {results['exam_weight']}%")
    lines.append("")

    grades = results["grades"]

    lines.append(f"  You need {grades['A+']}% on the final exam for an A+")
    lines.append(f"  You need {grades['A']}% on the final exam for an A")
    lines.append(f"  You need {grades['A-']}% on the final exam for an A-")
    lines.append(f"  You need {grades['B+']}% on the final exam for a B+")
    lines.append(f"  You need {grades['B']}% on the final exam for a B")
    if grades["Pass"] > 0:
        lines.append(f"  You need {grades['Pass']}% on the final exam to pass")

    lines.append("")
    return "\n".join(lines)

