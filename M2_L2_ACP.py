# My School Subject Planner (ACP starter, DSCM2L2). Python 3 standard library only.
# Run it in Google Colab (one cell) or as subject_planner.py. It runs now; do TODO 1 to TODO 4 in order.
# Lines marked (given) are done for you. Sets are printed with sorted() so the order never changes.

# (given) A: a fixed student card: (name, grade, section). It must not change.
card = ("Maya", 9, "B")

# TODO 1: print the name (index 0) and the grade and section together as a slice.
#   Check: "Student: Maya" and "Grade and section: (9, 'B')".
print("Student: ?")  # (given) placeholder: replace this line

# (given) B: the subjects as typed from the timetable (some are typed twice).
monday_list = ["Maths", "Science", "English", "Maths", "Art"]
tuesday_list = ["Maths", "History", "English", "Music", "History"]

# TODO 2: make the sets monday and tuesday from the two lists (duplicates disappear).
#   Check: "Monday: 4 ['Art', 'English', 'Maths', 'Science']".
monday = tuesday = set()  # (given) placeholder: replace this line
print("Monday:", len(monday), sorted(monday))

# TODO 3: Art moves to Wednesday: discard "Art" from monday. Add "Computing" to
#   tuesday. Discard "Dance" from monday too (it is not there: no crash).
#   Check: "Tuesday: ['Computing', 'English', 'History', 'Maths', 'Music']".
print("Monday:", sorted(monday))
print("Tuesday:", sorted(tuesday))

# TODO 4: print the subjects on both days, on either day, only on Monday, and on
#   exactly one of the two days (use the four set operations).
#   Check: "Both days: ['English', 'Maths']" and "Only Monday: ['Science']".
