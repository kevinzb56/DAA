import random
import pandas as pd
import os

# List of valid grades (2 characters each)
grades = ["AA", "AB", "BB", "BC", "CC", "CD", "DD", "FF"]

# Function to generate valid grade sequences of 40 characters (20 subjects)
def generate_valid_grades():
    return "".join(random.choice(grades) for _ in range(20))  # 40 characters for 20 subjects

# Function to generate negative test cases
def generate_negative_grades(case_type="small_length"):
    if case_type == "small_length":
        return "".join(random.choice(grades) for _ in range(10))  # 20 characters instead of 40
    elif case_type == "number_in_grades":
        return "".join(random.choice(grades) for _ in range(20))[:38] + "1A"  # Introducing a number in the grade sequence
    elif case_type == "special_characters":
        return "".join(random.choice(grades) for _ in range(20))[:38] + "$@"  # Adding special characters

# Function to generate CSV data
def generate_csv_data(file_name, valid=True, num_students=20):
    students_data = []

    for i in range(num_students):
        student_id = f"S{i+1}"
        if valid:
            grades_data = generate_valid_grades()
        else:
            # Randomly choose a type of invalid grade sequence
            case_type = random.choice(["small_length", "number_in_grades", "special_characters"])
            grades_data = generate_negative_grades(case_type)

        students_data.append({"Student ID": student_id, "Grades": grades_data})

    # Create a DataFrame
    df = pd.DataFrame(students_data)

    # Define the directory to save CSV files
    directory = "lcs_test_cases"
    os.makedirs(directory, exist_ok=True)

    # Save DataFrame to CSV
    file_path = os.path.join(directory, file_name)
    df.to_csv(file_path, index=False)
    print(f"CSV file '{file_name}' generated successfully in '{directory}'.")

# Generate 5 positive CSV files with valid grades (40 characters long)
for i in range(1, 6):
    generate_csv_data(f"positive_test_case_{i}.csv", valid=True)

# Generate 5 negative CSV files with invalid grades
for i in range(1, 6):
    generate_csv_data(f"negative_test_case_{i}.csv", valid=False)
