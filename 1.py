
marks = [78, 85, 92, 45, 67, 88, 98, 21, 35, 74, 82, 58, 63, 71, 89, 90, 32, 60, 77, 42]


total_students = len(marks)


highest_marks = max(marks)
lowest_marks = min(marks)


average_marks = sum(marks) / total_students


passing_marks = 40
passed_students = [m for m in marks if m >= passing_marks]
failed_students = [m for m in marks if m < passing_marks]


passed_count = len(passed_students)
failed_count = len(failed_students)


pass_percentage = (passed_count / total_students) * 100


sorted_marks = sorted(marks)


grades = {'Grade A': 0, 'Grade B': 0, 'Grade C': 0, 'Grade D': 0, 'Grade F': 0}

for mark in marks:
    if mark >= 85:
        grades['Grade A'] += 1
    elif mark >= 70:
        grades['Grade B'] += 1
    elif mark >= 55:
        grades['Grade C'] += 1
    elif mark >= 40:
        grades['Grade D'] += 1
    else:
        grades['Grade F'] += 1


print(f"Total Students: {total_students}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Average Marks: {average_marks:.1f}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Pass Percentage: {pass_percentage:.1f}%")


if len(sorted_marks) > 4:
    formatted_sorted = f"[{sorted_marks[0]}, {sorted_marks[1]}, {sorted_marks[2]}, ..., {sorted_marks[-1]}]"
else:
    formatted_sorted = str(sorted_marks)

print(f"Sorted Marks: {formatted_sorted}")

for grade, count in grades.items():
    print(f"{grade}: {count} Students")