# student_system.py
# Student Management System for a coaching institute

# Global list to store student records
# Each record: [name, subject, marks]
records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Sneha", "Chemistry", 83],
    ["Vikram", "Physics", 67],
    ["Pooja", "Math", 95],
    ["Arjun", "Chemistry", 78],
    ["Nisha", "Physics", 85],
    ["Karan", "Chemistry", 90],
    ["Divya", "Math", 72],
    ["Rohan", "Physics", 88],
    ["Meera", "Chemistry", 61],
]


def add_student(name, subject, marks):
    """Adds a student record, prevents duplicate name+subject combo."""
    # Check if same name + subject already exists
    for r in records:
        if r[0] == name and r[1] == subject:
            print(f"  [!] {name} already has a record for {subject}. Not added.")
            return
    records.append([name, subject, marks])
    print(f"  [+] Added: {name}, {subject}, {marks}")


def get_toppers(subject):
    """Returns top 3 students in a subject sorted by marks."""
    # Filter by subject then sort descending
    subject_records = [r for r in records if r[1] == subject]
    if not subject_records:
        print(f"  No records found for subject: {subject}")
        return []
    sorted_records = sorted(subject_records, key=lambda x: x[2], reverse=True)
    # Use slicing to get top 3
    return sorted_records[:3]


def class_average(subject):
    """Returns average marks for a given subject."""
    marks_list = [m[2] for m in records if m[1] == subject]
    if not marks_list:
        print(f"  No records found for subject: {subject}")
        return 0
    avg = sum(marks_list) / len(marks_list)
    return round(avg, 2)


def above_average_students():
    """Returns students scoring above the overall class average."""
    # Get all marks
    all_marks = [r[2] for r in records]
    if not all_marks:
        return []
    overall_avg = sum(all_marks) / len(all_marks)
    # Nested logic: filter students above overall average
    above_avg = [r for r in records if r[2] > overall_avg]
    return above_avg, round(overall_avg, 2)


def remove_student(name):
    """Remove all records of a student using list comprehension (not remove() in loop)."""
    global records
    before = len(records)
    # Safe removal using comprehension - avoids mutation during iteration
    records = [r for r in records if r[0] != name]
    after = len(records)
    removed = before - after
    if removed > 0:
        print(f"  [-] Removed {removed} record(s) for '{name}'.")
    else:
        print(f"  [!] No records found for '{name}'.")


def save_to_file():
    """Save all records to students.txt on exit."""
    with open("students.txt", "w") as f:
        f.write("Name,Subject,Marks\n")
        for r in records:
            f.write(f"{r[0]},{r[1]},{r[2]}\n")
    print("\n  [*] Records saved to students.txt")


def display_menu():
    print("\n========== Student Management System ==========")
    print("  1. Add Student")
    print("  2. Show Toppers (by subject)")
    print("  3. Show Class Average (by subject)")
    print("  4. Show Above-Average Students")
    print("  5. Remove Student")
    print("  6. Exit")
    print("================================================")


def main():
    while True:
        display_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            name = input("  Enter student name: ").strip()
            subject = input("  Enter subject (Math/Physics/Chemistry): ").strip()
            try:
                marks = int(input("  Enter marks: ").strip())
                add_student(name, subject, marks)
            except ValueError:
                print("  [!] Invalid marks. Please enter a number.")

        elif choice == "2":
            subject = input("  Enter subject: ").strip()
            toppers = get_toppers(subject)
            if toppers:
                print(f"\n  Top 3 in {subject}:")
                for i, t in enumerate(toppers, 1):
                    print(f"    {i}. {t[0]} - {t[2]} marks")

        elif choice == "3":
            subject = input("  Enter subject: ").strip()
            avg = class_average(subject)
            if avg:
                print(f"\n  Average marks in {subject}: {avg}")

        elif choice == "4":
            result = above_average_students()
            if result:
                students, overall_avg = result
                print(f"\n  Overall Average: {overall_avg}")
                print("  Students above average:")
                for s in students:
                    print(f"    {s[0]} | {s[1]} | {s[2]} marks")

        elif choice == "5":
            name = input("  Enter student name to remove: ").strip()
            remove_student(name)

        elif choice == "6":
            save_to_file()
            print("  Goodbye!\n")
            break

        else:
            print("  [!] Invalid choice. Try again.")


if __name__ == "__main__":
    main()
