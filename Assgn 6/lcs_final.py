
# import pandas as pd
# import re

# # Define the LCS function
# def lcs(str1, str2):
#     dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#     lcs_sequence = []
#     i, j = len(str1), len(str2)
#     while i > 0 and j > 0:
#         if str1[i - 1] == str2[j - 1]:
#             lcs_sequence.append(str1[i - 1])
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1

#     return ''.join(reversed(lcs_sequence))

# # Function to check the validity of the grades
# def validate_grades(grades):
#     if len(grades) != 40:
#         raise ValueError(f"Invalid grade sequence length: {grades}. Expected length is 40 characters.")
    
#     if any(char.isdigit() for char in grades):
#         raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")
    
#     if not all(re.match(r"[A-F]{2}", grades[i:i+2]) for i in range(0, len(grades), 2)):
#         raise ValueError(f"Invalid grade sequence: {grades}. Special characters or invalid grade format detected.")

# # Handle positive test cases
# print("Positive Test Cases:")
# for i in range(1, 5):
#     file_path = f"lcs_test_cases/positive_test_case_{i}.csv"
#     df = pd.read_csv(file_path)

#     # Extract the grades column as a list
#     grades_list = df["Grades"].tolist()

#     # Initialize LCS as the first student's grades
#     overall_lcs = grades_list[0]
#     for i in range(1, len(grades_list)):
#         try:
#             # Validate each student's grade sequence
#             validate_grades(grades_list[i])
#             # Calculate LCS only if the grades are valid
#             overall_lcs = lcs(overall_lcs, grades_list[i])
#         except ValueError as e:
#             print(f"Error for student {df.iloc[i]['Student ID']}: {e}")

#     print(f"Longest Common Subsequence of Grades for All Students in Test Case {i}:", overall_lcs)

# # Handle negative test cases
# print("\nNegative Test Cases:")
# for i in range(1, 5):
#     file_path = f"lcs_test_cases/negative_test_case_{i}.csv"
#     df = pd.read_csv(file_path)

#     # Extract the grades column as a list
#     grades_list = df["Grades"].tolist()

#     # Initialize LCS as the first student's grades
#     overall_lcs = grades_list[0]
#     error_found = False  # Flag to track if an error is found

#     for i in range(1, len(grades_list)):
#         try:
#             # Validate each student's grade sequence
#             validate_grades(grades_list[i])
#             # Calculate LCS only if the grades are valid
#             overall_lcs = lcs(overall_lcs, grades_list[i])
#         except ValueError as e:
#             print(f"Error for student {df.iloc[i]['Student ID']}: {e}")
#             error_found = True
#             break  # No need to process further if there's an error

#     if not error_found:
#         print(f"Longest Common Subsequence of Grades for All Students in Test Case {i}:", overall_lcs)
#     else:
#         print(f"Error detected in Test Case {i}. Skipping LCS calculation.")


# import pandas as pd
# import re
# import os

# # Define the LCS function
# def lcs(str1, str2):
#     dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#     lcs_sequence = []
#     i, j = len(str1), len(str2)
#     while i > 0 and j > 0:
#         if str1[i - 1] == str2[j - 1]:
#             lcs_sequence.append(str1[i - 1])
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1

#     return ''.join(reversed(lcs_sequence))

# # Function to check the validity of the grades
# def validate_grades(grades):
#     if len(grades) != 40:
#         raise ValueError(f"Invalid grade sequence length: {grades}. Expected length is 40 characters.")

#     if any(char.isdigit() for char in grades):
#         raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")

#     if not all(re.match(r"[A-F]{2}", grades[i:i+2]) for i in range(0, len(grades), 2)):
#         raise ValueError(f"Invalid grade sequence: {grades}. Special characters or invalid grade format detected.")

# # Function to process CSV files and compute LCS
# def process_csv_files(file_path):
#     df = pd.read_csv(file_path)
#     grades_list = df["Grades"].tolist()

#     # Initialize LCS as the first student's grades
#     overall_lcs = grades_list[0]

#     for i in range(1, len(grades_list)):
#         try:
#             # Validate each student's grade sequence
#             validate_grades(grades_list[i])
#             # Calculate LCS only if the grades are valid
#             overall_lcs = lcs(overall_lcs, grades_list[i])
#         except ValueError as e:
#             print(f"Error for student {df.iloc[i]['Student ID']}: {e}")
#             return None

#     return overall_lcs

# # Main function to run positive and negative test cases
# def main():
#     directory = "lcs_test_cases"

#     print("Positive Test Cases:")
#     # Start numbering from 1 for positive test cases
#     for i in range(1, 5):
#         file_path = os.path.join(directory, f"positive_test_case_{i}.csv")
#         lcs_result = process_csv_files(file_path)
#         if lcs_result is not None:
#             print(f"Longest Common Subsequence for Positive Test Case {i}: {lcs_result}")

#     print("\nNegative Test Cases:")
#     # Start numbering from 1 for negative test cases but separate it from positive test cases
#     for i in range(1, 5):
#         file_path = os.path.join(directory, f"negative_test_case_{i}.csv")
#         lcs_result = process_csv_files(file_path)
#         if lcs_result is not None:
#             print(f"Longest Common Subsequence for Negative Test Case {i}: {lcs_result}")
#         else:
#             print(f"Error detected in Negative Test Case {i}. Skipping LCS calculation.")

# if __name__ == "__main__":
#     main()


import pandas as pd
import re
import os


class LCSCalculator:
    """Handles the calculation of Longest Common Subsequence (LCS)."""

    def __init__(self):
        self.memo = None

    def compute_lcs_length(self, s1, s2):
        m, n = len(s1), len(s2)
        self.memo = [[-1] * (n + 1) for _ in range(m + 1)]
        return self._lcs_recursive(s1, s2, m, n)

    def _lcs_recursive(self, s1, s2, m, n):
        if m == 0 or n == 0:
            return 0

        if self.memo[m][n] != -1:
            return self.memo[m][n]

        if s1[m - 1] == s2[n - 1]:
            self.memo[m][n] = 1 + self._lcs_recursive(s1, s2, m - 1, n - 1)
        else:
            self.memo[m][n] = max(
                self._lcs_recursive(s1, s2, m - 1, n), self._lcs_recursive(s1, s2, m, n - 1)
            )
        return self.memo[m][n]

    def reconstruct_lcs(self, s1, s2):
        m, n = len(s1), len(s2)
        self.compute_lcs_length(s1, s2)  # Ensure the memo table is filled
        lcs_sequence = []
        while m > 0 and n > 0:
            if s1[m - 1] == s2[n - 1]:
                lcs_sequence.append(s1[m - 1])
                m -= 1
                n -= 1
            elif self.memo[m - 1][n] >= self.memo[m][n - 1]:
                m -= 1
            else:
                n -= 1
        return ''.join(reversed(lcs_sequence))


class GradeValidator:
    """Validates the grades sequence based on predefined rules."""

    @staticmethod
    def validate(grades):
        if len(grades) != 6:
            raise ValueError(f"Invalid grade sequence length: {grades}. Expected length is 40 characters.")
        if any(char.isdigit() for char in grades):
            raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")
        if not all(re.match(r"[A-F]{2}", grades[i:i + 2]) for i in range(0, len(grades), 2)):
            raise ValueError(f"Invalid grade sequence: {grades}. Special characters or invalid grade format detected.")


class CSVProcessor:
    """Handles CSV file reading and processing for LCS computation."""

    def __init__(self, lcs_calculator, grade_validator):
        self.lcs_calculator = lcs_calculator
        self.grade_validator = grade_validator

    def process_file(self, file_path):
        df = pd.read_csv(file_path)
        grades_list = df["Grades"].tolist()

        # Initialize LCS as the first student's grades
        overall_lcs = grades_list[0]

        for i in range(1, len(grades_list)):
            try:
                self.grade_validator.validate(grades_list[i])
                overall_lcs = self.lcs_calculator.reconstruct_lcs(overall_lcs, grades_list[i])
            except ValueError as e:
                print(f"Error for student {df.iloc[i]['Student ID']}: {e}")
                return None

        return overall_lcs


class Application:
    """Main application class to run the program."""

    def __init__(self, csv_processor, directory):
        self.csv_processor = csv_processor
        self.directory = directory

    def run_test_cases(self, test_type, start=1, end=5):
        print(f"{test_type.capitalize()} Test Cases:")
        for i in range(start, end):
            file_path = os.path.join(self.directory, f"{test_type}_test_case_{i}.csv")
            lcs_result = self.csv_processor.process_file(file_path)
            if lcs_result is not None:
                print(f"Longest Common Subsequence for {test_type.capitalize()} Test Case {i}: {lcs_result}")
            else:
                print(f"Error detected in {test_type.capitalize()} Test Case {i}. Skipping LCS calculation.")


if __name__ == "__main__":
    # Adhering to Dependency Inversion Principle by injecting dependencies
    lcs_calculator = LCSCalculator()
    grade_validator = GradeValidator()
    csv_processor = CSVProcessor(lcs_calculator, grade_validator)

    app = Application(csv_processor, "lcs_test_cases")

    # Run positive and negative test cases
    app.run_test_cases("positive")
    app.run_test_cases("negative")
