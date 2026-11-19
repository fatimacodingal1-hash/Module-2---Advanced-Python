# School Class Organiser (complete activity, DSCM2L1). Python 3 standard library only.
# Run: python school_class_organiser.py  (or paste into one Google Colab cell and press Run)
# Time: O(n log n) overall, because sort() is the slowest step; every other step is O(n) or O(1).
# Space: O(n) for the list and the dictionaries (n = number of students).

# A. Step 1: a list of classmates in the order they joined.
classmates = ["Aiden", "Paula", "Ricky", "Sonia", "Dan"]
print("Class list:", classmates)

# Step 2: read the list without changing it.
print("Total students:", len(classmates))
print("First:", classmates[0], "| Last:", classmates[-1])
print("First three:", classmates[:3])


# Step 3: change the list.
def remove_student(names, name):
    """Remove name only if it is in the list. O(n): 'in' and remove() each walk the list."""
    if name in names:
        names.remove(name)
        return True
    return False


classmates.append("Maria")                                    # B: O(1), adds to the end
leaver = input("Which student leaves the class? ")
print("Remove", leaver + ":", remove_student(classmates, leaver))
print("Remove Kevin (not in class):", remove_student(classmates, "Kevin"))
classmates.sort()                                             # C: O(n log n), A to Z
print("Sorted:", classmates)

# D. Step 4: a dictionary, where each key is a label for one value.
teacher = {"name": "Mr. Smith", "subject": "Python", "experience": 5}
print("\nTeacher:", teacher)

# Step 5: read, update, add and remove keys.
print("Subject:", teacher["subject"])
print("Email:", teacher.get("email", "Not found"))
teacher["experience"] = 6
teacher["room"] = "Lab 2"
teacher.pop("experience")
print("Updated teacher:", teacher)

# Step 6: two lists that line up, position by position.
roll_numbers = [1, 2, 3, 4, 5]                                 # E
directory = dict(zip(roll_numbers, classmates))
print("\nDirectory:", directory)


def find_by_roll(book, roll):
    """O(1) on average: a dictionary jumps straight to the key."""
    return book.get(roll, "No student with that roll number")


roll = int(input("Roll number to look up? "))
print(f"Roll {roll}:", find_by_roll(directory, roll))
print("Roll 9:", find_by_roll(directory, 9))                  # F: edge case, missing key
empty_class = []                                              # G: edge case, empty list
print("Empty class:", len(empty_class), empty_class[:3], remove_student(empty_class, "Dan"))
