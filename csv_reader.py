import csv
import os
from final_mark import percentages

def manual_input():
    marks_needed = {}
    try:
        num_courses = int(input("Number of courses: "))
    except Exception:
        print("\n\nlol misinput TRY AGAIN\n\n")
        return manual_input()

    for _ in range(num_courses):
        course = input("Course Name: ")
        while True:
            try:
                mark_earned = float(input("The weight of all marks before the exam: "))
                mark_loss = float(input("Marks Lost (in %): "))
                bonus_string = input("Enter the weight of any bonuses (press Enter if none): ")
                bonus = float(bonus_string) if bonus_string.strip() else 0.0
                break
            except Exception:
                print("\nlol misinput TRY AGAIN\n")
        marks_needed[course] = percentages(mark_earned, mark_loss, bonus)
    return marks_needed

def csv_input(filename):
    marks_needed = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            course = row["Course"]
            try:
                mark_earned = float(row["MarkEarned"])
                mark_loss = float(row["MarkLoss"])
                bonus = float(row["Bonus"]) if row["Bonus"] else 0.0
            except Exception as e:
                print(f"Error in row for {course}: {e}")
                continue
            marks_needed[course] = percentages(mark_earned, mark_loss, bonus)
    return marks_needed

def write_output(marks_needed, output_filename="marks_needed.txt"):
    with open(output_filename, "w") as file:
        for course, marks in marks_needed.items():
            file.write(f"{course}\n")
            file.write(f"A+ --> {marks['A+']}%\n")
            file.write(f"A  --> {marks['A']}%\n")
            file.write(f"A- --> {marks['A-']}%\n")
            file.write(f"Pass --> {marks['Pass']}%\n\n")

def main():
    use_csv = input("Read courses from CSV file? (y/n): ").lower().strip()
    if use_csv == 'y':
        filename = input("Enter CSV filename (default: courses.csv): ").strip() or "courses.csv"
        if not os.path.exists(filename):
            print(f"File '{filename}' not found. Switching to manual input.\n")
            marks_needed = manual_input()
        else:
            marks_needed = csv_input(filename)
    else:
        marks_needed = manual_input()
    write_output(marks_needed)
    print("Done! Results written to 'marks_needed.txt'.")

if __name__ == "__main__":
    main()
