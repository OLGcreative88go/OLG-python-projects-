print("===== STUDENT PROFILE GENERATOR =====")

name = input("What is your name? ")
department = input("What department are you? ")
level = input("What level are you? ")

print("\n===== YOUR PROFILE =====")
print("Name:", name)
print("Department:", department)
print("Level:", level)

if level == "100":
    print("Welcome, 100-level student!")
elif level == "200":
    print("Welcome, 200-level student!")
elif level == "300":
    print("Welcome, 300-level student!")
elif level == "400":
    print("Welcome, 400-level student!")
else:
    print("Invalid level. Please enter 100, 200, 300, or 400.")

print("Keep learning Python. Your future is bright!")

