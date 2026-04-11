ABSENT = int(input("Enter the number of days absent: "))
PRESENT = int(input("Enter the number of days present: "))
total_days = ABSENT + PRESENT
print("Total days:", total_days)
attendance_percentage = (PRESENT / total_days) * 100
print("Attendance percentage:", attendance_percentage)
if attendance_percentage >= 75:
    print("The student is eligible to take the exam.")
else:
    print("The student is not eligible to take the exam.")
