# Class Student (complete activity 1, DSCM2L3). Python 3 standard library only.
# Run: python class_student.py  (or paste into one Google Colab cell and press Run)


# A: the class keyword makes a blueprint called Student.
class Student:
    # B: this print is in the class body. Python runs the body ONCE, when it reads
    # the class, not each time an object is made. Count how often you see this line.
    print("Python read the Student blueprint.")
    school = "Sunrise School"        # C: a class variable, shared by every Student
    # Step 1: Add a class variable
    grade = 10
    print("Class variable grade:", grade)


# Step 2: Make two objects
anna = Student()
ryan = Student()
print("anna is a", type(anna))                                 # D

# Step 3: Read shared class variables
print("anna's school:", anna.school, "| ryan's grade:", ryan.grade)
new_grade = int(input("New class grade? "))
Student.grade = new_grade
print("After changing the class grade: anna", anna.grade, "| ryan", ryan.grade)

# Step 4: Edge case: give one object its own value
anna.grade = 12
print("anna", anna.grade, "| ryan", ryan.grade, "| Student", Student.grade)
print("\n")

print("Activity no. 2")
# Class Student - 2 (complete activity 2, DSCM2L3). Python 3 standard library only.
# Run: python class_student_2.py  (or paste into one Google Colab cell and press Run)


class Student:
    school = "Sunrise School"                                  # A: class variable

    def introduction(self):
        """A method: a function inside the class. self is the object it is called on."""
        # Step 1: First method
        return "Hi, I am a student at " + self.school

    def details(self):
        # Step 2: Method that reads the object's own data
        return f"My name is {self.name} and I study in grade {self.grade}."


anna = Student()                                               # B: one object
anna.name = input("Student name? ")                                             # C: data stored on
anna.grade = int(input("Grade? "))                                                #    this object only
print(anna.introduction())
print(anna.details())
print(Student.details(anna))   # D: the same call written out; self is anna

# Step 3: Same methods, another object
ryan = Student()
ryan.name = "Ryan"
ryan.grade = 9
print(ryan.details())
print("\n")

print("Activity no. 3")
# Parrot Bird (complete activity 3, DSCM2L3). Python 3 standard library only.
# Run: python parrot_bird.py  (or paste into one Google Colab cell and press Run)


class Parrot:
    species = "bird"                                           # A: class variable

    def __init__(self, name, age):
        """Runs by itself every time a Parrot is made: Parrot("Blu", 10)."""
        # Step 1: Instance variables
        self.name = name
        if age < 0:
            age = 0
        self.age = age


# Step 2: Make two parrots
parrot_name = input("Name of the first parrot? ")
blu = Parrot(parrot_name, 10)
woo = Parrot("Woo", 15)
print(blu.name, "is a", blu.species)                          # B: class variable
print(woo.name, "is also a", Parrot.species)                  #    read two ways
print(blu.name, "is", blu.age, "years old")                   # C: instance
print(woo.name, "is", woo.age, "years old")                   #    variables

# Step 3: Edge case: bad age
ghost = Parrot("Ghost", -3)
print(ghost.name, "is", ghost.age, "years old")
print("\n")

print("Activity no. 4")
# Parrot Bird - II (complete activity 4, DSCM2L3). Python 3 standard library only.
# Run: python parrot_bird_2.py  (or paste into one Google Colab cell and press Run)


class Parrot:
    species = "bird"                                           # A

    def __init__(self, name, age):                             # B: from activity 3
        self.name = name
        if age < 0:                                            # the same age check as activity 3
            age = 0
        self.age = age

    def sing(self, song):
        # Step 1: Method with a parameter
        if song == "":
            return f"{self.name} hums quietly."
        return f"{self.name} sings {song}"

    def dance(self):
        # Step 2: Method with no extra parameter
        return f"{self.name} is now dancing"

    def birthday(self):
        # Step 3: Method that changes the object
        self.age = self.age + 1
        return self.age


parrot_name = input("Name of the first parrot? ")
blu = Parrot(parrot_name, 10)                                        # C: two objects
woo = Parrot("Woo", 15)
song = input("Which song does the parrot sing? ")
print(blu.sing(song))                                       # D: calling methods
print(blu.sing(""))                                            #    edge case: empty song
print(blu.dance())
print("After the birthday", blu.name, "is", blu.birthday())
print(woo.name, "is still", woo.age)                           # E: woo is not changed
